import PySimpleGUI as sg
# import TkEasyGUI as sg

# ラベルとボタンを配置したレイアウト --- (*1)
layout = [
  [sg.Text("知恵はサンゴに勝り，他のどんな望ましいものもそれにはかなわない。")],
  [sg.Button("OK")]
]
# ウィンドウを表示する --- (*2)
window = sg.Window("格言", layout)
# イベントループ --- (*3)
while True:
    # ウィンドウからイベントを取得する --- (*4)
    event, values = window.read()
    # 閉じるボタンの処理 --- (*5)
    if event == sg.WINDOW_CLOSED:
        break
    # OKボタンが押された時の処理 --- (*6)
    if event == "OK":
        sg.popup("OKボタンが押されました")
        break
# 終了処理
window.close()
