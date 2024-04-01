import os
import TkEasyGUI as sg

# 保存ファイル名を指定 --- (*1)
SCRIPT_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(SCRIPT_DIR, "notepad-save-data.txt")
# メモ帳のレイアウトの定義 --- (*2)
layout = [
    [sg.Multiline(size=(40, 15), key="text")],
    [sg.Button("保存"), sg.Button("開く")],
]
window = sg.Window("メモ帳", layout=layout)
# イベントループ --- (*3)
while True:
    # イベントと入力値の取得 --- (*4)
    event, values = window.read()
    # 閉じるボタンを押した時
    if event == sg.WINDOW_CLOSED:
        break
    # 「保存」ボタンを押した時 --- (*5)
    if event == "保存":
        # ファイルに保存
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            f.write(values["text"])
        sg.popup("保存しました")
    # 「開く」ボタンを押した時 --- (*6)
    if event == "開く":
        # 保存先のファイルが存在するか確認 --- (*7)
        if not os.path.exists(SAVE_FILE):
            sg.popup("一度も保存されていません")
            continue
        # 保存されたファイルを読み込む --- (*8)
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            text = f.read()
        # 読んだ内容をテキストボックスに反映 --- (*9)
        window["text"].update(text)
# 終了処理
window.close()
