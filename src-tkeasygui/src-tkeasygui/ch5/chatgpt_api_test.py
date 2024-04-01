from openai import OpenAI

# ChatGPTに質問する関数を定義 --- (*1)
def ask_chatgpt(prompt, model = "gpt-3.5-turbo"):
    # ChatGPTのAPIを使うためにOpenAIオブジェクトを作成 --- (*2)
    client = OpenAI()
    # あるいは、client = OpenAI(api_key="sk-xxxxxx")
    # ChatGPTのAPIを使って質問をする --- (*3)
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}])
    # ChatGPTの回答を返す --- (*4)
    return completion.choices[0].message.content

if __name__ == "__main__":
    # ChatGPTに質問する --- (*5)
    q = "猫が主人公の小説のあらすじを起承転結で考えてください。"
    print(f"> {q}")
    print(ask_chatgpt(q))
