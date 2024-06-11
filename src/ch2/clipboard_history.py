import os
import json
import pyperclip
import PySimpleGUI as sg
# import TkEasyGUI as sg

# クリップボードの履歴を保存するファイルパス --- (*1)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(ROOT_DIR, 'clipboard-history.json')
# 保存する履歴の最大数
MAX_HISTORY = 20

# 既存の履歴を読み込む --- (*2)
history = []
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
# 履歴を保存する
def save_history():
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
# 履歴を整形する --- (*3)
def list_format(history):
    crlf = lambda v: v.strip().replace("\r", "").replace("\n", "¶")
    short = lambda v: v[:20] + "..." if len(v) > 20 else v
    return [f"{i+1:02}: {crlf(short(h))}" for i, h in enumerate(history)]
# レイアウトを指定 --- (*4)
layout = [
    [sg.Text("履歴を選んで「コピー」ボタンをクリックしてください。")],
    [sg.Listbox( # クリップボードの履歴 --- (*4a)
            values=list_format(history),
            size=(40, 15),
            font=("Arial", 14),
            key="-history-")
    ],
    [
        # 各種ボタン --- (*4b)
        sg.Button("コピー"), sg.Button("削除"), sg.Button("終了")
    ],
]
# ウィンドウを作成する ---- (*5)
window = sg.Window("クリップボード履歴管理", layout)
# イベントループ
while True:
    # イベントを取得する
    event, values = window.read(timeout=100)
    # 閉じるボタンが押されたら終了
    if event in [sg.WINDOW_CLOSED, "終了"]:
        break
    # コピーボタンを押した時 --- (*6)
    if event == "コピー":
        # 選択された履歴をクリップボードにコピー
        sel_text = values["-history-"][0]
        # 実際の履歴データを取り出す
        index = int(sel_text[0:2])
        text = history[index - 1]
        pyperclip.copy(text)
        sg.popup("クリップボードにコピーしました")
    # 削除ボタンを押したら履歴を削除 --- (*7)
    if event == "削除":
        sel_text = values["-history-"][0]
        # 実際の履歴データを取り出す
        index = int(sel_text[0:2])
        del history[index - 1]
        window["-history-"].update(list_format(history))
        save_history()
        pyperclip.copy("") # 重複登録しないようにクリップボードをクリア
        sg.popup("削除しました")
    # 定期的にクリップボードの内容をチェック --- (*8)
    text = pyperclip.paste()
    if text == "":
        continue # 空なら何もしない
    if text not in history: # 履歴に追加
        history.insert(0, text)
        if len(history) > MAX_HISTORY: # 履歴が多すぎる場合は削除
            history.pop()
        # リストボックスを更新
        window["-history-"].update(list_format(history))
        save_history()
        continue
    # 履歴の順番を入れ替え --- (*9)
    index = history.index(text)
    if index > 0:
        del history[index] # 既存の履歴を削除
        history.insert(0, text) # 先頭に追加
        # リストボックスを更新
        window["-history-"].update(list_format(history))
        save_history()
window.close()
