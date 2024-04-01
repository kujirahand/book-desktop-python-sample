import TkEasyGUI as sg

# ラベルが1つだけのウィンドウを作成する
window = sg.Window("ウィンドウ", [[sg.Text("一番簡単なウィンドウ")]])
# イベントループ
while True:
    # ウィンドウからイベントを取得する
    event, values = window.read()
    # 閉じるボタンの処理
    if event == sg.WINDOW_CLOSED:
        break
window.close()
