import memo_ai_template as mat
import memo_ai_app
import datetime

# テンプレートに機能を追加 --- (*1)
mat.TEMPLATES["軽快なジョーク"] = f"""
親しい友人に手紙を書くのですが、ユーモアたっぷりのジョークから始めたいです。
どうか、気が利いていて軽快で、最高のジョークを教えてください。
"""
mat.TEMPLATES["話題提供"] = f"""
あまり親しくない知人に挨拶を送る必要があります。
どうか、当たり障りのない話題を提供してください。
天気以外の話題で、3-5文の具体的な文面をいくつか考えて下さい。
"""
# 時候の挨拶をテンプレートに追加 --- (*2)
now = datetime.datetime.now() # 現在日時を取得
mat.TEMPLATES["時候の挨拶"] = f"""
お客様に、丁寧な手紙を書く必要があります。
{now.month}月に相応しい時候の挨拶をいくつか考えてください。
"""

if __name__ == "__main__":
    memo_ai_app.ai_functions = mat.TEMPLATES.keys()
    memo_ai_app.show_window()

