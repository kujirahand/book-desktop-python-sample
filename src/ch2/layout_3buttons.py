import PySimpleGUI as sg
# import TkEasyGUI as sg

# ラベルとボタンを配置したレイアウト
layout = [
    [sg.Text("信号は何色になったら進んで良いでしょうか？")], # 1行目
    [sg.Button("青"), sg.Button("黄"), sg.Button("赤")], # 2行目 
]
# ウィンドウを表示する
window = sg.Window("ボタンを3つ並べる例", layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED: break
window.close()
