import TkEasyGUI as sg

# ラベルとボタンを配置したレイアウト --- (*1)
layout = [
    [sg.Text("1行目のラベル")], # 1行目 
    [sg.Text("2行目のラベル")], # 2行目 
    [sg.Text("3行目のラベル")], # 3行目 
]
# ウィンドウを表示する
window = sg.Window("レイアウトの例", layout)
while True: # イベントループ
    event, values = window.read()
    if event == sg.WINDOW_CLOSED: break
window.close()
