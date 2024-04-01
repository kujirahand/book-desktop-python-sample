import TkEasyGUI as sg

# ボタンを使って、九九の表を作る
# Y方向のループ --- (*1)
layout = [[]]
for no in range(1, 10+1):
    # ボタンを作成 --- (*2)
    btn = sg.Button(
        no, # ボタンのラベル
        key=f"-btn", # キー(わざと重複するキーを指定)
        size=(3, 1) # ボタンのサイズを指定
    )
    layout[0].append(btn)
# ウィンドウを作成する --- (*3)
window = sg.Window("重複するキー", layout)
# イベントループ --- (*4)
while True:
    # ウィンドウからイベントを取得する --- (*5)
    event, _ = window.read()
    # 閉じるボタンの処理 --- (*6)
    if event == sg.WINDOW_CLOSED:
        break
    # ボタンが押された時 ---- (*7)
    if event.startswith("-btn"):
        # ボタンのキーからラベルを取り出す --- (*8)
        label = window[event].ButtonText
        sg.popup(f"[{label}]ボタン(key={event})が押されました！")
window.close()
