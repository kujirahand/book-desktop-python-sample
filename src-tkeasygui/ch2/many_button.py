import TkEasyGUI as sg

# 10個のボタンを一度に作成する --- (*1)
layout = [[]]
for no in range(1, 10+1):
    # ボタンを作成 --- (*2)
    btn = sg.Button(
        f"{no}", # ボタンのラベル
        key=f"-btn{no}", # キー
        size=(3, 1) # ボタンのサイズを指定
    )
    # レイアウトに追加 --- (*3)
    layout[0].append(btn)
# ウィンドウを作成する --- (*4)
window = sg.Window("たくさんのボタン", layout)
# イベントループ --- (*5)
while True:
    # ウィンドウからイベントを取得する --- (*6)
    event, _ = window.read()
    # 閉じるボタンの処理
    if event == sg.WINDOW_CLOSED:
        break
    # ボタンが押された時 ---- (*7)
    if event.startswith("-btn"):
        sg.popup(event + 'が押されました')
window.close()