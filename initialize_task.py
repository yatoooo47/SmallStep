# タスク初期化スクリプト
from app import db, Task
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:0407@localhost:5432/Small_Step'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 初期タスクデータ
tasks = [
            {
            "task_level": 1,
            "task_name": "起床後に顔を洗う",
            "task_description": "朝起きた後に顔を洗い、気分をリフレッシュします。"
            },
            {       
            "task_level": 1,
            "task_name": "部屋の窓を開けて換気をする",
            "task_description": "部屋の空気を入れ替えるために窓を開けます。"
            },
            {
            "task_level": 1,
            "task_name": "5分間の軽いストレッチを行う",
            "task_description": "5分間体をほぐすために軽いストレッチを行います。"
            },
            {
            "task_level": 2,
            "task_name": "洗濯物を一回回す",
            "task_description": "洗濯機で洗濯物を回します。"
            },
            {
            "task_level": 2,
            "task_name": "10分間の散歩をする",
            "task_description": "10分間外を歩いて体を動かします。"
            },
            {
            "task_level": 2,
            "task_name": "次の日の服を準備する",
            "task_description": "次の日に着る服をあらかじめ準備しておきます。"
            },
            {
            "task_level": 2,
            "task_name": "水を1リットル飲む",
            "task_description": "水を1リットル飲んで体を水分補給します。"
            },
            {
            "task_level": 2,
            "task_name": "朝食を食べる",
            "task_description": "朝食を食べて1日のエネルギーを補給します。"
            },
            {
            "task_level": 3,
            "task_name": "近所のスーパーまで歩く",
            "task_description": "スーパーまで歩いて買い物をします。"
            },
            {
            "task_level": 3,
            "task_name": "部屋の1箇所を掃除する",
            "task_description": "部屋の1箇所を掃除して、整理整頓します。"
            },
            {
            "task_level": 3,
            "task_name": "手帳やスマホに翌日の予定を書き込む",
            "task_description": "翌日の予定を手帳やスマホに書き込んで整理します。"
            },
            {
            "task_level": 3,
            "task_name": "20分間読書をする",
            "task_description": "本を20分間読んで知識を深めます。"
            },
            {
            "task_level": 3,
            "task_name": "ゴミを出す",
            "task_description": "家のゴミを出して部屋を清潔に保ちます。"
            },
            {
            "task_level": 3,
            "task_name": "一日中、一定の時間ごとにストレッチをする",
            "task_description": "体をほぐすために一定の時間ごとにストレッチを行います。"
            },
            {
            "task_level": 3,
            "task_name": "短い瞑想をする（5分）",
            "task_description": "5分間の瞑想で心を落ち着かせます。"
            },
            {
            "task_level": 4,
            "task_name": "友人や家族に1通のメッセージを送る",
            "task_description": "友人や家族に1通のメッセージを送ってコミュニケーションをとります。"
            },
            {
            "task_level": 4,
            "task_name": "冷蔵庫の中を整理する",
            "task_description": "冷蔵庫を整理し、食品を新鮮に保ちます。"
            },
            {
            "task_level": 4,
            "task_name": "駅やバス停まで歩いて行く",
            "task_description": "駅やバス停まで歩いて、外の空気を感じます。"
            },
            {
            "task_level": 4,
            "task_name": "部屋の模様替えの計画を立てる",
            "task_description": "部屋の模様替えを計画して新しいレイアウトを考えます。"
            },
            {
            "task_level": 4,
            "task_name": "軽い運動（15分）",
            "task_description": "15分間の軽い運動を行い、体をほぐします。"
            },
            {
            "task_level": 4,
            "task_name": "自炊する（簡単な食事でもOK）",
            "task_description": "自炊をして健康的な食事を作ります。"
            },
            {
            "task_level": 4,
            "task_name": "ToDoリストを作成する",
            "task_description": "今日やるべきことをToDoリストに書き出して整理します。"
            },
            {
            "task_level": 4,
            "task_name": "本を1章読む",
            "task_description": "本を1章読んで知識を深めます。"
            },
            {
            "task_level": 4,
            "task_name": "30分間スクリーンタイムを減らす（スマホやPCの使用を控える）",
            "task_description": "スマホやPCの使用を30分間控えます。"
            },
            {
            "task_level": 5,
            "task_name": "近所のカフェや公共施設に行く",
            "task_description": "カフェや公共施設に行って外出の練習をします。"
            },
            {
            "task_level": 5,
            "task_name": "職場や学校に関連する情報を1件調べる",
            "task_description": "職場や学校に関する情報を調べて、最新の情報を得ます。"
            },
            {
            "task_level": 5,
            "task_name": "1日のスケジュールを立てる",
            "task_description": "1日のスケジュールを計画して効率的に過ごします。"
            },
            {
            "task_level": 5,
            "task_name": "簡単なエクササイズを30分行う",
            "task_description": "体を動かして健康的な生活習慣を作ります。"
            },
            {
            "task_level": 5,
            "task_name": "昨日やったタスクの進捗を振り返る",
            "task_description": "昨日のタスクの進捗を振り返り、反省点や改善点を見つけます。"
            },
            {
            "task_level": 5,
            "task_name": "10分間、自己成長に関する動画や記事を視聴する",
            "task_description": "自己成長に役立つコンテンツを視聴して学びます。"
            },
            {
            "task_level": 5,
            "task_name": "野菜を1種類使って料理する",
            "task_description": "1種類の野菜を使って料理を作り、健康的な食生活を実践します。"
            },
            {
            "task_level": 5,
            "task_name": "近所を30分散歩する",
            "task_description": "近所を散歩して、外の空気を楽しみます。"
            },
            {
            "task_level": 5,
            "task_name": "1時間スマホやPCの使用を控える",
            "task_description": "スマホやPCの使用を1時間控えて、休憩を取ります。"
            },
            {
            "task_level": 5,
            "task_name": "日記に自分の感想を書く",
            "task_description": "1日の感想や気づきを日記に書きます。"
            },
            {
            "task_level": 6,
            "task_name": "友人や知り合いと電話で会話する",
            "task_description": "友人や知り合いと電話でコミュニケーションを取ります。"
            },
            {
            "task_level": 6,
            "task_name": "自分の興味のある分野に関する本や記事を30分読む",
            "task_description": "自分の興味に関連した本や記事を30分間読みます。"
            },
            {
            "task_level": 6,
            "task_name": "1週間のメニューを考える",
            "task_description": "1週間の食事メニューを考え、計画を立てます。"
            },
            {
            "task_level": 6,
            "task_name": "お金を使わずに楽しめる活動を1つ実践する",
            "task_description": "お金を使わずに楽しめる活動を実践してみます。"
            },
            {
            "task_level": 6,
            "task_name": "外出して新しい場所を訪れる",
            "task_description": "外に出て、新しい場所を訪れることで外出の自信を高めます。"
            },
            {
            "task_level": 6,
            "task_name": "1時間自分の趣味に集中する",
            "task_description": "自分の趣味に1時間集中して時間を過ごします。"
            },
            {
            "task_level": 6,
            "task_name": "週の目標を3つ設定する",
            "task_description": "1週間の目標を3つ設定して、達成を目指します。"
            },
            {
            "task_level": 6,
            "task_name": "予定の確認と更新をする",
            "task_description": "今後の予定を確認し、必要な変更を加えます。"
            },
            {
            "task_level": 6,
            "task_name": "新しい料理に挑戦する",
            "task_description": "新しい料理を作って、料理のスキルを向上させます。"
            },
            {
            "task_level": 6,
            "task_name": "1日の終わりにリラックスする時間を作る",
            "task_description": "1日の終わりにリラックスする時間を取って、心身を癒やします。"
            },
            {
            "task_level": 7,
            "task_name": "求人情報を1件調べる",
            "task_description": "求人情報を1件調べ、就職活動に向けた第一歩を踏み出します。"
            },
            {
            "task_level": 7,
            "task_name": "図書館や公園などで新しい場所を訪れる",
            "task_description": "図書館や公園など、新しい場所を訪れて外出の機会を作ります。"
            },
            {
            "task_level": 7,
            "task_name": "自己啓発のために新しいスキルや趣味を始める",
            "task_description": "自己啓発のために新しいスキルや趣味に挑戦します。"
            },
            {
            "task_level": 7,
            "task_name": "1時間、積極的に運動する",
            "task_description": "1時間をかけて積極的に運動を行い、体を健康に保ちます。"
            },
            {
            "task_level": 7,
            "task_name": "3つの短期目標を立てる",
            "task_description": "達成可能な短期目標を3つ立て、進捗を追います。"
            },
            {
            "task_level": 7,
            "task_name": "1つのチャリティーやボランティア活動について調べる",
            "task_description": "チャリティーやボランティア活動を1つ調べ、参加の準備をします。"
            },
            {
            "task_level": 7,
            "task_name": "知り合いと昼食やお茶に行く",
            "task_description": "知り合いと昼食やお茶を共にし、交流を深めます。"
            },
            {
            "task_level": 7,
            "task_name": "次の週のタスク計画を作る",
            "task_description": "次週のタスク計画を立て、準備を整えます。"
            },
            {
            "task_level": 7,
            "task_name": "自分のスキルに関連するオンラインコースを調べる",
            "task_description": "自分のスキル向上に役立つオンラインコースを調べます。"
            },
            {
            "task_level": 7,
            "task_name": "自己紹介を練習する（鏡の前で）",
            "task_description": "自己紹介を鏡の前で練習し、自信を持って話せるようにします。"
            },
            {
            "task_level": 8,
            "task_name": "就職活動の計画を立てる",
            "task_description": "就職活動の具体的な計画を立て、ステップを決めます。"
            },
            {
            "task_level": 8,
            "task_name": "履歴書や職務経歴書の書き方を調べる",
            "task_description": "履歴書や職務経歴書の書き方を調べ、書き方をマスターします。"
            },
            {
            "task_level": 8,
            "task_name": "近所の施設を1つ訪れる",
            "task_description": "近所にある施設を訪れ、環境に慣れるための活動を行います。"
            },
            {
            "task_level": 8,
            "task_name": "新しいレシピに挑戦して食事を作る",
            "task_description": "新しいレシピを試して、料理スキルを向上させます。"
            },
            {
            "task_level": 8,
            "task_name": "1時間以上の運動を行う",
            "task_description": "体を動かして健康を維持するために1時間以上の運動を行います。"
            },
            {
            "task_level": 8,
            "task_name": "過去1週間のタスク進捗を振り返る",
            "task_description": "過去1週間のタスクを振り返り、進捗と改善点を分析します。"
            },
            {
            "task_level": 8,
            "task_name": "知人に連絡を取って進展を共有する",
            "task_description": "知人に連絡を取り、現在の進捗を共有します。"
            },
            {
            "task_level": 8,
            "task_name": "自分のスキルや興味に関連する講座やイベントを探す",
            "task_description": "自分のスキルや興味に関連する講座やイベントを調べ、参加の準備をします。"
            },
            {
            "task_level": 8,
            "task_name": "お金を使わずに楽しむ方法を3つ考える",
            "task_description": "お金を使わずに楽しめる方法を3つ考えて、実践します。"
            },
            {
            "task_level": 8,
            "task_name": "朝早く起きて、少なくとも3時間集中して活動する",
            "task_description": "朝早く起きて、集中して活動する時間を3時間確保します。"
            },
            {
            "task_level": 8,
            "task_name": "自分の考えや感情を整理するために日記を書く",
            "task_description": "自分の考えや感情を整理するために日記をつけます。"
            },
            {
            "task_level": 9,
            "task_name": "職業訓練やセミナーに申し込む",
            "task_description": "職業訓練やセミナーに申し込んで、スキルアップの機会を作ります。"
            },
            {
            "task_level": 9,
            "task_name": "将来のキャリア計画を立てる",
            "task_description": "将来のキャリアプランを立て、目標達成に向けた道筋を決めます。"
            },
            {
            "task_level": 9,
            "task_name": "2時間の集中作業を行う",
            "task_description": "2時間集中して作業し、効率よくタスクを進めます。"
            },
            {
            "task_level": 9,
            "task_name": "知り合いとプロフェッショナルな話題について話す",
            "task_description": "知り合いとプロフェッショナルな話題について会話を交わします。"
            },
            {
            "task_level": 9,
            "task_name": "模擬面接の練習をする",
            "task_description": "面接の練習を行い、実際の面接に備えます。"
            },
            {
            "task_level": 9,
            "task_name": "週次のタスクの進捗報告を作成する",
            "task_description": "週次の進捗を報告し、必要に応じて計画を調整します。"
            },
            {
            "task_level": 9,
            "task_name": "SNSやLinkedInで専門分野に関するアカウントをフォローする",
            "task_description": "SNSやLinkedInで専門分野に関するアカウントをフォローして、ネットワークを広げます。"
            },
            {
            "task_level": 9,
            "task_name": "一日中、健康的な食事を心がける",
            "task_description": "1日を通して健康的な食事を意識して摂取します。"
            },
            {
            "task_level": 9,
            "task_name": "自分の短期目標を振り返る",
            "task_description": "短期目標を振り返り、進捗や課題を確認します。"
            },
            {
            "task_level": 9,
            "task_name": "週の計画を再評価し、修正する",
            "task_description": "今週の計画を再評価し、必要な修正を加えます。"
            },
            {
            "task_level": 9,
            "task_name": "自分を褒めるためにリラックスタイムを取る",
            "task_description": "1週間の成果を振り返り、自分を褒めるためにリラックスします。"
            },
            {
            "task_level": 9,
            "task_name": "新しい趣味を深掘りする",
            "task_description": "新しい趣味をさらに深掘りして、知識を広げます。"
            },
            {
            "task_level": 10,
            "task_name": "1日中規則正しい生活を心がける",
            "task_description": "規則正しい生活を送るため、1日を計画的に過ごします。"
            },
            {
            "task_level": 10,
            "task_name": "求人に1件応募する",
            "task_description": "求人情報を見て、1件応募します。"
            },
            {
            "task_level": 10,
            "task_name": "2時間以上の集中作業を行う",
            "task_description": "2時間以上、集中して作業を行い、高い生産性を維持します。"
            },
            {
            "task_level": 10,
            "task_name": "模擬面接を実際にやってみる",
            "task_description": "実際に模擬面接を行い、面接準備を万全にします。"
            },
            {
            "task_level": 10,
            "task_name": "運動を1時間以上行う",
            "task_description": "健康を維持するために1時間以上運動を行います。"
            },
            {
            "task_level": 10,
            "task_name": "リーダーシップに関する記事や動画を視聴する",
            "task_description": "リーダーシップに関する学びを深めるために、記事や動画を視聴します。"
            },
            {
            "task_level": 10,
            "task_name": "将来のキャリア目標を再確認し、細かく計画を練る",
            "task_description": "将来のキャリア目標を細かく計画し、進むべき方向を決めます。"
            },
            {
            "task_level": 10,
            "task_name": "誰かとコラボレーションするプロジェクトを考える",
            "task_description": "コラボレーションの機会を生かして、新しいプロジェクトを考えます。"
            },
            {
            "task_level": 10,
            "task_name": "ネットワーキングのための人と繋がる（オンライン/オフライン）",
            "task_description": "ネットワーキング活動を行い、プロフェッショナルなつながりを広げます。"
            },
            {
            "task_level": 10,
            "task_name": "自分のスキルや知識を他人に教える",
            "task_description": "自分の知識やスキルを他人に教えて、成長を促進します。"
            },
            {
            "task_level": 10,
            "task_name": "週の達成度を高く維持するために新しいチャレンジを見つける",
            "task_description": "週の達成度を維持するため、新しいチャレンジを見つけて取り組みます。"
            },
            {
            "task_level": 10,
            "task_name": "自分の成果を具体的に振り返り、次のステップを決める",
            "task_description": "自分の成果を振り返り、次のステップに向けて具体的な行動計画を立てます。"
            },
            {
            "task_level": 10,
            "task_name": "今週の全てのタスクを完了する",
            "task_description": "今週のすべてのタスクを完了し、達成感を得ます。"
            }
    ]


with app.app_context():
    for task_data in tasks:
        task = Task.query.filter_by(task_name=task_data["task_name"]).first()
        if not task:  # 重複を避ける
            new_task = Task(
                task_level=task_data["task_level"],
                task_name=task_data["task_name"],
                task_description=task_data["task_description"]
            )
            db.session.add(new_task)
    db.session.commit()
    print("タスクが初期化されました！")
