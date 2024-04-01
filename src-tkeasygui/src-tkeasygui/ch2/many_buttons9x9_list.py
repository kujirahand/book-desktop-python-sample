import TkEasyGUI as sg
# リストの内包表記で九九のボタンを作成
layout = []
for y in range(1, 9+1):
    layout.append([sg.Button(
        x*y, key=f"-btn{x}x{y}", size=(3,1)) for x in range(1, 9+1)])
window = sg.Window("九九の表", layout)
while True: # イベントループ
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED: break
window.close()
