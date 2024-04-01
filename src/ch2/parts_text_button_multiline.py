import PySimpleGUI as sg
# import TkEasyGUI as sg

# レイアウトを作成する
layout = [
    # テキストラベル
    [sg.Text("ABCを実行しますか？")],
    # ボタン
    [sg.Button("実行する")],
    # 複数行のエディタ
    [sg.Multiline(size=(40, 3), default_text="テキスト", key="text")], 
]
# ウィンドウを表示する
window = sg.Window("パーツを利用する例", layout)
# イベントループ
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED: break
window.close()
