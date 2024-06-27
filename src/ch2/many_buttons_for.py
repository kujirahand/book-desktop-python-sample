import PySimpleGUI as sg
# import TkEasyGUI as sg
# 10個のボタンを一度に作成する --- (*1)
layout = [[]]
for no in range(1, 10+1):
    # ボタンを作成 --- (*2)
    btn = sg.Button(f"{no}", size=(3, 1))
    # レイアウトに追加 --- (*3)
    layout[0].append(btn)
# ウィンドウを表示 --- (*4)
window = sg.Window("たくさんのボタン", layout)
while True:
    e, _ = window.read()
    if e == sg.WINDOW_CLOSED: break
window.close()
