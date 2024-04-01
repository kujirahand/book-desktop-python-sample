import PySimpleGUI as sg
# import TkEasyGUI as sg

# ラベルを配置したウィンドウを表示する --- (*1)
layout = [[sg.Text("怠け者は欲しがるが何も得ず、勤勉な人は十分に満たされる。")]]
window = sg.Window("格言", layout)
# イベントループ --- (*2)
while True:
    # ウィンドウからイベントを取得する --- (*3)
    event, values = window.read()
    # 閉じるボタンを押したらループから抜ける --- (*4)
    if event == sg.WINDOW_CLOSED:
        break
# 終了処理 --- (*5)
window.close()
