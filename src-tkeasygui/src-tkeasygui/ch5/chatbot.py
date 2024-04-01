from openai import OpenAI

# 会話の内容を保持するリストを定義 --- (*1)
messages = [
    # システムに与える初期プロンプトを指定 --- (*2)
    {
        "role": "system",
        "content": "あなたは論理的で優秀なAIアシスタントです。"
    }
]

# ChatGPTと会話する関数を定義 --- (*3)
def chat_chatgpt(prompt, model = "gpt-3.5-turbo"):
    # 今回のユーザーのプロンプトをmessagesに追加 --- (*4)
    messages.append({"role": "user", "content": prompt})
    # messagesの内容を確認したい場合、以下の2行のコメントを外す
    # import json
    # print(json.dumps(messages, indent=2, ensure_ascii=False))
    # ChatGPTのAPIを使って質問をする --- (*5)
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=messages)
    # ChatGPTの回答を取得 --- (*6)
    content = completion.choices[0].message.content
    # 次回の会話のためにChatGPTの回答を記録 --- (*7)
    messages.append({"role": "assistant", "content": content})
    return content

if __name__ == "__main__":
    # ChatGPTに連続で質問する --- (*8)
    print("### これからチャットボットと会話をしましょう")
    print("### [q] で終了します。")
    while True:
        user = input("あなた> ")
        if user == "q": quit()
        if user == "": continue
        bot = chat_chatgpt(user)
        print("ボット>", bot)
        print("---")
