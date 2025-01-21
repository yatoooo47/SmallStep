from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_kind = db.Column(db.Integer, nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_level = db.Column(db.Integer, nullable=False)
    task_name = db.Column(db.String(255), nullable=False)
    task_description = db.Column(db.Text, nullable=True)

class UserTaskProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

class UserTag(db.Model):
    __tablename__ = 'user_tag'
    id = db.Column(db.Integer, primary_key=True)
    executor_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False)
    approver_id = db.Column(db.String(255), db.ForeignKey('user.user_id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
