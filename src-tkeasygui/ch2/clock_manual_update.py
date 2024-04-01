import datetime
import TkEasyGUI as sg

# 現在時刻を文字列で取得する関数 --- (*1)
def get_time_str():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")
# デジタル時計のレイアウトを指定 --- (*2)
layout = [
    [sg.Text(get_time_str(), key="-output-", font=("Helvetica", 80))],
    [sg.Button("時間の更新", font=("Helvetica", 20))]
]
# ウィンドウを作成する --- (*3)
window = sg.Window("不完全なデジタル時計", layout)
# イベントループ --- (*4)
while True:
    # イベントを取得する --- (*5)
    event, _ = window.read()
    # 閉じるボタンが押されたら終了
    if event == sg.WINDOW_CLOSED:
        break
    # 時間の更新ボタンを押したら、現在時刻を取得して表示 --- (*6)
    if event == "時間の更新":
        window["-output-"].update(get_time_str())
window.close()
