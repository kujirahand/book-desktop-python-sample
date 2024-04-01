import TkEasyGUI as eg

# ウィンドウを表示する
window = eg.Window(
    title="格言を表示するアプリ",
    layout=[[eg.Text("以下のボタンを押してください。")],
            [eg.Button("格言を表示")]])
# イベントループを開始
while window.is_alive():
    event, _ = window.read() # イベントを読む
    if event == "格言を表示": # ボタンを押した時の処理
        eg.popup("良い言葉によって心が晴れる")
window.close()
