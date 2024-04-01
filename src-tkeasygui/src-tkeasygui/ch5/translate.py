from openai import OpenAI

# 英日翻訳を行うためのプロンプトのテンプレート --- (*1)
TEMPLATE = """
### 指示:
下記の入力を日本語に翻訳してください。
その際、子供でも分かるように平易な言葉で翻訳してください。
### 入力:
__INPUT__
"""

# ChatGPTに質問する関数を定義 --- (*2)
def ask_chatgpt(prompt, model = "gpt-3.5-turbo"):
    # ChatGPTのAPIを使うためにOpenAIオブジェクトを作成 --- (*3)
    client = OpenAI()
    # ChatGPTのAPIを使って質問をする --- (*4)
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}])
    # ChatGPTの回答を返す --- (*5)
    return completion.choices[0].message.content

# 英日翻訳を行う関数を定義 --- (*6)
def translate(text_english):
    # テンプレートにデータを差し込む --- (*7)
    prompt = TEMPLATE.replace("__INPUT__", text_english)
    # APIを呼び出して結果を返す
    result = ask_chatgpt(prompt)
    return result

if __name__ == "__main__":
    print("### 英日翻訳ツール")
    print("### 英語の文章を入力してください。[q]で終了します。")
    # 連続で翻訳を行う
    while True:
        # ユーザーからの入力を得る --- (*8)
        text = input(">>> ")
        text = text.strip()
        if text == "": continue
        if text == "q": break
        # 翻訳実行 --- (*9)
        print(translate(text))
