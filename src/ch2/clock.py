import datetime
import PySimpleGUI as sg
# import TkEasyGUI as sg

# デジタル時計のレイアウトを指定
layout = [
    [sg.Text("00:00:00", key="-output-", font=("Helvetica", 80))]
]
# ウィンドウを作成する
window = sg.Window("デジタル時計(完成版)", layout)
# イベントループ
while True:
    # イベントを取得する --- (*1)
    event, _ = window.read(timeout=10)
    # 閉じるボタンが押されたら終了
    if event == sg.WINDOW_CLOSED:
        break
    # 現在時刻を取得して表示
    now = datetime.datetime.now()
    window["-output-"].update(
        now.strftime("%H:%M:%S")
    )
