from datetime import datetime
import PySimpleGUI as sg
# import TkEasyGUI as sg

# デジタル時計を最前面に表示 --- (*1)
window = sg.Window("時計",
    layout=[[sg.Text("x", enable_events=True, font=("", 8)),
             sg.Text("--:--:--", key="-clock-")]], 
    no_titlebar=True, # タイトルバーのないウィンドウ
    keep_on_top=True, # 最前面表示 (Windowsのみ)
    grab_anywhere=True, # 掴んで動かせるように
    font=("Arial", 40),
    finalize=True)
# イベントループ --- (*2)
while True:
    event, values = window.read(timeout=100, timeout_key="-timeout-")
    if event in [sg.WIN_CLOSED, "x"]: # 閉じる
        break
    if event == "-timeout-": # タイムアウトで更新
        now_s = datetime.now().strftime("%H:%M:%S")
        window["-clock-"].update(now_s)
window.close()

