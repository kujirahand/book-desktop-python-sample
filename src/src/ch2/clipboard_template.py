import os
import sys
import pyperclip
import PySimpleGUI as sg
# import TkEasyGUI as sg

# テンプレートファイルのパスを指定 --- (*1)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'template-files')

# システムフォントを選択 --- (*2)
fonts = {"win32": ("メイリオ", 12), "darwin": ("Hiragino Sans", 14)}
font = fonts[sys.platform] if sys.platform in fonts else ("Arial", 16)

# テンプレートファイルの一覧を取得する --- (*3)
def get_template_files():
    files = os.listdir(TEMPLATE_DIR)
    files = [f for f in files if f.endswith('.txt')]
    return files

# レイアウトを指定 --- (*4)
layout = [
    [sg.Text("テンプレートファイルを選択してください")],
    [
        sg.Listbox( # 画面左側のファイル一覧のリストボックス --- (*4a)
            values=get_template_files(), 
            size=(40, 20), 
            key="-files-", 
            enable_events=True,
            font=font
        ),
        # 画面右側のテンプレートの内容を表示するテキストボックス --- (*4b)
        sg.Multiline(size=(40, 20), key="-body-", font=font)
    ],
    [
        sg.Button("内容をコピー", font=font), # 各種ボタン --- (*4c)
        sg.Button("ファイル一覧を更新", font=font), 
        sg.Button("終了", font=font)
    ],
]
# ウィンドウを作成する ---- (*5)
window = sg.Window("クリップボードテンプレート", layout)
# イベントループ
while True:
    # イベントを取得する
    event, values = window.read()
    # 閉じるボタンが押されたら終了
    if event in [sg.WINDOW_CLOSED, "終了"]:
        break
    # ファイルを選択したら内容を読み込む --- (*6)
    if event == "-files-":
        filename = values["-files-"][0]
        filepath = os.path.join(TEMPLATE_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            window["-body-"].update(text)
    # コピーボタンを押したらクリップボードにコピー --- (*7)
    if event == "内容をコピー":
        body = values["-body-"] # 内容を取得
        pyperclip.copy(body) # クリップボードにコピー
        # 長すぎる場合は省略して表示
        body = body if len(body) < 64 else body[0:64] + "..."
        sg.popup(body, title="クリップボードにコピーしました")
    # ファイル更新ボタンを押したらリストボックスを更新 --- (*8)
    if event == "ファイル一覧更新":
        files = get_template_files()
        window["-files-"].update(files)
window.close()
