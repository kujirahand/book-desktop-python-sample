import TkEasyGUI as sg

# ウィンドウを表示する
win = sg.Window(
    title="格言を表示するアプリ",
    layout=[[sg.Text("以下のボタンを押してください。")],
            [sg.Button("格言を表示")]])
# イベントループを開始
while True:
    event, _ = win.read() # イベントを読む
    if event == sg.WIN_CLOSED: break
    if event == "格言を表示": # ボタンを押した時の処理
        sg.popup("良い言葉によって心が晴れる")
