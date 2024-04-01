from threading import Thread
from queue import Queue
import PySimpleGUI as sg
# import TkEasyGUI as sg
import chatbot

# 翻訳テンプレートの指定 --- (*1)
TEMPLATE = """
指示: 次の入力を日本語に翻訳してください。
入力: ```__INPUT__```
"""
# 翻訳ツールの初期プロンプトを指定 --- (*2)
chatbot.messages = [{
    "role": "system",
    "content": "あなたは子供向け英日翻訳ツールです。"
}]
# イベントやデータをやり取りするためのキュー --- (*3)
ui_que = Queue()
# 翻訳ツールのGUIを表示する --- (*4)
def show_window():
    layout = [
        [sg.Text("英語を入力してください:")],
        [
            sg.Multiline(size=(40, 3),key="input"),
            sg.Button("翻訳", key="exec-button")
        ],
        [sg.Text("英日翻訳ボットとの会話")],
        [sg.Multiline(size=(50, 40), key="output", background_color="#f0f0f0")]
    ]
    win = sg.Window("会話に対応した英日翻訳ツール", layout)
    # イベントループを開始 --- (*5)
    while True:
        event, values = win.read(timeout=100, timeout_key="-TIMEOUT-")
        if event == sg.WIN_CLOSED:
            break
        # 「翻訳」ボタンを押した時の処理 --- (*6)
        if event == "exec-button":
            user = values["input"]
            # ボタンを押せないようにして、入力ボックスをクリア
            win["exec-button"].update(disabled=True)
            win["input"].update("")
            # 結果のテキストボックスに色を付けて出力 --- (*7)
            win["output"].print("<USER>",
                text_color="white", background_color="green")
            win["output"].print(user,
                text_color="black", background_color="#f0fff0")
            # スレッドでChatGPTへの問い合わせを実行 --- (*8)
            th = Thread(target=translate_work, args=(user,))
            th.start()
        # タイムアウトした時の処理
        if event == "-TIMEOUT-":
            # ui_queからデータを取り出す
            if ui_que.empty(): continue
            ui_event, ui_values = ui_que.get_nowait()
            # 翻訳が完了した時の処理 --- (*9)
            if ui_event == "done":
                win["exec-button"].update(disabled=False)
                # 結果のテキストボックスに色を付けて出力
                win["output"].print("<BOT>",
                    text_color="white", background_color="blue")
                win["output"].print(ui_values["output"],
                    text_color="black", background_color="#f0f0ff")

# 日英翻訳を行う関数 --- (*10)
def translate_work(user):
    # 初回の会話なら、テンプレートに埋め込む
    if len(chatbot.messages) == 1:
        user = TEMPLATE.replace("__INPUT__", user)
    result = chatbot.chat_chatgpt(user)
    # 完了イベントををキューに追加
    ui_que.put(["done", {"output": result}])

if __name__ == "__main__":
    show_window()
