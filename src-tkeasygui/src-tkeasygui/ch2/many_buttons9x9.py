import TkEasyGUI as sg

# ボタンを使って、九九の表を作る
# Y方向のループ --- (*1)
layout = []
for y in range(1, 9+1):
    # X方向のループ --- (*2)
    buttons = []
    for x in range(1, 9+1):
        # ボタンを作成 --- (*3)
        label = str(y * x) # 計算結果をラベルとする
        btn = sg.Button(
            label, # ボタンのラベル
            key=f"-btn{x}x{y}", # キー
            size=(3, 1) # ボタンのサイズを指定
        )
        # ボタンを変数buttonsに追加
        buttons.append(btn)
    # レイアウトに変数buttonsを追加
    layout.append(buttons)
# ウィンドウを作成する --- (*4)
window = sg.Window("九九の表", layout)
# イベントループ --- (*5)
while True:
    # ウィンドウからイベントを取得する --- (*6)
    event, _ = window.read()
    # 閉じるボタンの処理
    if event == sg.WINDOW_CLOSED:
        break
    # ボタンが押された時 ---- (*7)
    if event.startswith("-btn"):
        # ボタンのキーからラベルを取り出す --- (*8)
        label = window[event].ButtonText
        sg.popup(f"{event}={label}が押されました！")
window.close()
