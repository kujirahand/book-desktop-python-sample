# ChatGPT APIに与えるmessagesの例
messages = [
  # 初期プロンプトの指定
  {
    "role": "system",
    "content": "あなたは論理的で優秀なAIアシスタントです。"
  },
  # ユーザーのプロンプト(1回目)
  {
    "role": "user",
    "content": "白い猫の名前を一つ考えて"
  },
  # ChatGPTの回答
  {
    "role": "assistant",
    "content": "「ホワイトニー」という名前はいかがでしょうか？"
  },
  # ユーザーのプロンプト(2回目)
  {
    "role": "user",
    "content": "どうしてその名前なの？"
  }
]
