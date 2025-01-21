from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import uuid
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.secret_key = 'Small_Step_app'


# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:0407@localhost:5432/Small_Step'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# データベースとマイグレーションの初期化
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


# ユーザーモデルの定義
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_kind = db.Column(db.Integer, nullable=False)


# タスクモデルの定義
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_level = db.Column(db.Integer, nullable=False)
    task_name = db.Column(db.String(255), nullable=False)
    task_description = db.Column(db.Text, nullable=True)


# ユーザーのタスク進捗を記録するモデル
class UserTaskProgress(db.Model):
    __tablename__ = 'user_task_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False, extend_existing=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False, extend_existing=True)
    is_completed = db.Column(db.Boolean, default=False, extend_existing=True)
    comment = db.Column(db.Text, nullable=True, extend_existing=True)
    is_approved = db.Column(db.Boolean, default=False, extend_existing=True)  # 新規カラム



# タッグモデル
class UserTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    executor_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False)
    approver_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="approved")  # 初期値を設定

    executor = db.relationship('User', foreign_keys=[executor_id])
    approver = db.relationship('User', foreign_keys=[approver_id])


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(name=name).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.user_id
        session['user_kind'] = user.user_kind
        if user.user_kind == 1:  # 実行ユーザー
            return redirect(url_for('task_management'))
        else:  # 承認ユーザー
            return redirect(url_for('approval_tasks'))

    flash("ログインに失敗しました。", "danger")
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        user_kind = int(request.form.get('user_kind', 1))
        user_id = str(uuid.uuid4())[:8]
        hashed_password = generate_password_hash(password)
        new_user = User(user_id=user_id, name=name, password=hashed_password, user_kind=user_kind)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/task_management', methods=['GET'])
def task_management():
    user_id = session.get('user_id')  # セッションからユーザーIDを取得
    if not user_id:
        return redirect(url_for('login'))

    # 現在のユーザー情報を取得
    current_user = User.query.filter_by(user_id=user_id).first()

    if current_user.user_kind == 2:  # 承認者の場合
        flash("タスク管理画面は承認者には表示されません。", "danger")
        return redirect(url_for('approval_tasks'))

    tasks_by_level = {}
    for task in Task.query.all():
        level = task.task_level
        if level not in tasks_by_level:
            tasks_by_level[level] = []

        progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task.id).first()
        if not progress:
            progress = UserTaskProgress(user_id=user_id, task_id=task.id, is_completed=False)
            db.session.add(progress)
            db.session.commit()

        tasks_by_level[level].append((task, progress, progress.is_approved))

    return render_template(
        'task_management.html',
        tasks_by_level=tasks_by_level,
        current_user=current_user
    )





@app.route('/submit_comment/<int:task_id>', methods=['POST'])
def submit_comment(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    comment = request.form.get('comment')
    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id).first()
    if not progress:
        progress = UserTaskProgress(user_id=user_id, task_id=task_id, is_completed=False)
    
    progress.comment = comment
    progress.is_completed = True

    # データベース保存処理に try-except を追加
    try:
        db.session.add(progress)
        db.session.commit()
        print("データベースに保存されました:", progress)
    except Exception as e:
        db.session.rollback()
        print("エラー発生:", str(e))
        flash("データの保存に失敗しました。", "danger")
        return redirect(url_for('task_submission', task_id=task_id))

    flash("感想が送信されました。", "success")
    return redirect(url_for('task_management'))

@app.route('/update_progress/<int:task_id>', methods=['POST'])
def update_progress(task_id):
    user_id = session.get('user_id')
    user_kind = session.get('user_kind')  # ユーザーの種類を取得
    if not user_id:
        return redirect(url_for('login'))
    
    # 実行者（user_kind == 1）だけが操作可能
    if user_kind != 1:
        flash("権限がありません。", "danger")
        return redirect(url_for('task_management'))

    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id).first()
    if not progress:
        progress = UserTaskProgress(user_id=user_id, task_id=task_id, is_completed=True)
        db.session.add(progress)
    else:
        progress.is_completed = True
    db.session.commit()
    flash("タスクを完了としてマークしました。", "success")
    return redirect(url_for('task_management'))


@app.route('/completed_tasks')
def completed_tasks():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # 現在のユーザー情報を取得
    current_user = User.query.filter_by(user_id=user_id).first()

    # ユーザーが達成済みのタスクを取得
    completed_tasks = UserTaskProgress.query.filter_by(user_id=user_id, is_completed=True).all()

    # タスクと進捗を取得
    tasks = [(Task.query.get(progress.task_id), progress) for progress in completed_tasks]

    return render_template('completed_tasks.html', tasks=tasks, current_user=current_user)






@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/task_submission/<int:task_id>')
def task_submission(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # 指定された task_id のタスクを取得
    task = Task.query.get(task_id)
    if not task:
        return "指定されたタスクは存在しません。", 404

    # タスクの進捗状況を取得
    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id).first()
    task.is_completed = progress.is_completed if progress else False

    return render_template('task_submission.html', task=task)


@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # タスク進捗を更新
    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id).first()
    if progress:
        progress.is_completed = True
    else:
        progress = UserTaskProgress(user_id=user_id, task_id=task_id, is_completed=True)
        db.session.add(progress)
    
    db.session.commit()
    return redirect(url_for('confirmation'))

@app.route('/completed_task_detail/<int:task_id>')
def completed_task_detail(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # タスク情報を取得
    task = Task.query.get(task_id)
    if not task:
        return "タスクが見つかりません", 404

    # タスク進捗状況を取得
    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id, is_completed=True).first()
    if not progress:
        return "指定されたタスクは達成されていません。", 404

    # 実行者の情報を取得
    executor = User.query.filter_by(user_id=progress.user_id).first()

    # 現在のユーザー情報を取得
    current_user = User.query.filter_by(user_id=user_id).first()

    return render_template(
        'completed_task_detail.html',
        task=task,
        progress=progress,
        current_user=current_user,
        executor=executor
    )




@app.route('/approval_tasks')
def approval_tasks():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # 必要以上に flash を呼び出さないよう確認
    tasks = db.session.query(
        Task.id.label('task_id'),
        Task.task_name,
        Task.task_description,
        User.name.label('executor_name'),
        UserTaskProgress.is_completed
    ).join(UserTaskProgress, Task.id == UserTaskProgress.task_id) \
     .join(User, UserTaskProgress.user_id == User.user_id) \
     .join(UserTag, UserTag.executor_id == User.user_id) \
     .filter(
         UserTag.approver_id == user_id,
         UserTaskProgress.is_completed == True,
         UserTag.status == "approved"
     ).all()

    current_user = User.query.filter_by(user_id=user_id).first()
    return render_template('approval_tasks.html', tasks=tasks, current_user=current_user)




@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/approve_tag/<int:tag_id>', methods=['POST'])
def approve_tag(tag_id):
    tag_request = UserTag.query.get(tag_id)
    if tag_request:
        tag_request.status = "approved"
        db.session.commit()
        flash("タッグリクエストを承認しました。", "success")
    else:
        flash("指定されたタッグリクエストが見つかりません。", "danger")
    return redirect(url_for('manage_tags'))



@app.route('/reject_task_progress/<int:task_id>', methods=['POST'])
def reject_task_progress(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    # タスク進捗を削除
    task_progress = UserTaskProgress.query.filter_by(task_id=task_id).first()
    if task_progress:
        db.session.delete(task_progress)  # レコードを削除
        db.session.commit()

    flash("タスク進捗を却下しました", "danger")
    return redirect(url_for('approval_tasks'))



@app.route('/manage_tags')
def manage_tags():
    if 'user_id' not in session or session.get('user_kind') != 2:
        return redirect(url_for('login'))

    approver_id = session['user_id']  # 現在の承認者ID
    pending_requests = UserTag.query.filter_by(approver_id=approver_id, status="pending").all()

    return render_template('manage_tags.html', pending_requests=pending_requests)



@app.route('/reject_tag/<int:tag_id>', methods=['POST'])
def reject_tag(tag_id):
    if 'user_id' not in session or session.get('user_kind') != 2:
        return redirect(url_for('login'))

    tag_request = UserTag.query.get(tag_id)
    if tag_request and tag_request.approver_id == session['user_id']:
        tag_request.status = "rejected"
        db.session.commit()
        flash("タッグリクエストを拒否しました。", "danger")

    return redirect(url_for('manage_tags'))

@app.route('/check_progress')
def check_progress():
    progresses = UserTaskProgress.query.all()
    result = []
    for progress in progresses:
        result.append(f"User: {progress.user_id}, Task: {progress.task_id}, Completed: {progress.is_completed}")
    return "<br>".join(result)

@app.route('/send_tag_request', methods=['POST'])
def send_tag_request():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    executor_id = session['user_id']  # 現在ログイン中のユーザーID
    approver_id = request.form.get('approver_id')  # フォームから入力された承認者ID

    if not approver_id:
        flash("承認者IDを入力してください。", "danger")
        return redirect(url_for('task_management'))

    # 既存のリクエストが存在するか確認
    existing_request = UserTag.query.filter_by(executor_id=executor_id, approver_id=approver_id).first()
    if existing_request:
        flash("すでにこの承認者にタッグリクエストを送っています。", "warning")
        return redirect(url_for('task_management'))

    # 新しいタッグリクエストを作成
    new_tag_request = UserTag(
        executor_id=executor_id,
        approver_id=approver_id,
        #status="pending"
    )
    db.session.add(new_tag_request)
    db.session.commit()

    flash("タッグリクエストを送信しました。", "success")
    return redirect(url_for('task_management'))

@app.route('/task_detail/<int:task_id>')
def task_detail(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # タスク詳細を取得
    task = Task.query.get(task_id)
    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id).first()

    if not task or not progress:
        flash("指定されたタスクが見つかりません。", "danger")
        return redirect(url_for('completed_tasks'))

    return render_template(
        'user_task_detail.html',
        task=task,
        progress=progress  # progressをテンプレートに渡す
    )


@app.route('/approve_task/<int:task_id>', methods=['POST'])
def approve_task(task_id):
    user_id = session.get('user_id')  # 承認者のIDを取得
    if not user_id:
        flash("ログインしてください。", "danger")
        return redirect(url_for('login'))

    # 現在のユーザー情報を取得
    current_user = User.query.filter_by(user_id=user_id).first()
    if not current_user or current_user.user_kind != 2:  # 承認者のみがアクセス可能
        flash("承認権限がありません。", "danger")
        return redirect(url_for('approval_tasks'))

    # タスク進捗情報を取得
    progress = UserTaskProgress.query.filter_by(task_id=task_id).first()
    if progress:
        if not progress.is_approved:  # 既に承認されていない場合
            progress.is_approved = True
            db.session.commit()  # 承認状態を保存
            flash("タスクを承認しました。", "success")
        else:
            flash("このタスクは既に承認されています。", "info")
    else:
        flash("タスクが見つかりません。", "danger")

    return redirect(url_for('approval_tasks'))







@app.route('/reject_task/<int:task_id>', methods=['POST'])
def reject_task(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # タスク進捗を削除
    progress = UserTaskProgress.query.filter_by(task_id=task_id).first()
    if progress:
        db.session.delete(progress)
        db.session.commit()

    flash("タスクを却下しました。", "danger")
    return redirect(url_for('approval_tasks'))



@app.route('/task_result')
def task_result():
    status = request.args.get('status')
    return render_template('task_result.html', status=status)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_level = request.form.get('task_level')
        task_name = request.form.get('task_name')
        task_description = request.form.get('task_description')

        new_task = Task(
            task_level=int(task_level),
            task_name=task_name,
            task_description=task_description
        )
        db.session.add(new_task)
        db.session.commit()
        flash("新しいタスクが追加されました！", "success")
        return redirect(url_for('task_management'))

    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/task_approval_detail/<int:task_id>')
def task_approval_detail(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # タスクと進捗状況を取得
    task = Task.query.get(task_id)
    progress = UserTaskProgress.query.filter_by(task_id=task_id, is_completed=True).first()

    if not task or not progress:
        return "タスクが見つからないか進捗情報が存在しません", 404

    # 実行者（executor）を取得
    executor = User.query.filter_by(user_id=progress.user_id).first()

    # 承認者（current_user）の情報を取得
    current_user = User.query.filter_by(user_id=user_id).first()

    return render_template(
        'task_approval_detail.html',
        task=task,
        progress=progress,
        executor=executor,
        current_user=current_user
    )

@app.route('/user_task_detail/<int:task_id>')
def user_task_detail(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    # 実行者向けのタスク詳細を取得
    task = Task.query.get(task_id)
    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id).first()

    if not task or not progress:
        flash("指定されたタスクが見つかりません。", "danger")
        return redirect(url_for('completed_tasks'))

    return render_template(
        'user_task_detail.html',
        task=task,
        progress=progress
    )

@app.route('/submit_task/<int:task_id>', methods=['POST'])
def submit_task(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    progress = UserTaskProgress.query.filter_by(user_id=user_id, task_id=task_id).first()
    if progress:
        progress.is_completed = True  # タスクは送信済み
        progress.is_approved = False  # 承認待ち
        db.session.commit()
        flash("タスクを送信しました。承認を待っています。", "info")
    else:
        flash("タスクが見つかりません。", "danger")
    
    return redirect(url_for('task_management'))

