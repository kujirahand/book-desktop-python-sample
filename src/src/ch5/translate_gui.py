from threading import Thread
from queue import Queue
import translate

import PySimpleGUI as sg
# import TkEasyGUI as sg

# イベントやデータをやり取りするためのキュー --- (*1)
ui_que = Queue()
# 翻訳ツールのGUIを表示する --- (*2)
def show_window():
    layout = [
        [sg.Text("以下に英文を入力してください。")],
        [sg.Multiline(size=(60, 5), key="input")],
        [sg.Button("英日翻訳", key="exec-button")],
        [sg.Text("翻訳結果(日本語):")],
        [sg.Multiline(size=(60, 5), key="output")]
    ]
    win = sg.Window("英日翻訳ツール", layout)
    # イベントループを開始 --- (*3)
    while True:
        event, values = win.read(timeout=100, timeout_key="-TIMEOUT-")
        if event == sg.WIN_CLOSED:
            break
        # 「英日翻訳」ボタンを押した時の処理 --- (*4)
        if event == "exec-button":
            win["exec-button"].update(disabled=True)
            win["output"].update("少々お待ちください。")
            th = Thread(target=translate_work, args=(values,))
            th.start()
        # タイムアウトした時の処理--- (*5)
        if event == "-TIMEOUT-":
            # ui_queからデータを取り出す
            if ui_que.empty(): continue
            ui_event, ui_values = ui_que.get_nowait()
            # 翻訳が完了した時の処理 --- (*6)
            if ui_event == "done":
                win["exec-button"].update(disabled=False)
                win["output"].update(ui_values["output"])

# 日英翻訳を行う関数 --- (*7)
def translate_work(values):
    result = translate.translate(values["input"])
    # 完了イベントををキューに追加 --- (*8)
    ui_que.put(["done", {"output": result}])

if __name__ == "__main__":
    show_window()
