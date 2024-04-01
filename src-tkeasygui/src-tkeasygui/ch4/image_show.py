import os
import TkEasyGUI as sg

# 画像ファイルのパスを指定 --- (*1)
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'image.png')
# レイアウトを定義 --- (*2)
layout = [
    [sg.Image(image_path)],
    [sg.Button('閉じる')]
]
# ウィンドウを作成 --- (*3)
window = sg.Window('画像の表示', layout)
# イベントループ --- (*4)
while True:
    # イベントの読み込み
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "閉じる":
        break
window.close()
