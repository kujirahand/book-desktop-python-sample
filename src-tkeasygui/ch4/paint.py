import TkEasyGUI as sg
from PIL import ImageGrab

# 描画を行うキャンバスを定義 -- (*1)
canvas = sg.Canvas(size=(400, 400), key="-canvas-", background_color="red")
# ウィンドウを作成 --- (*2)
window = sg.Window("マウス操作で絵を描こう", layout=[
    [canvas],
    [sg.Button("閉じる"), sg.Button("保存")],
], finalize=True)
# マウスイベントが発生するように指定 --- (*3)
canvas.bind("<ButtonPress>", "b_press")
canvas.bind("<ButtonRelease>", "b_release")
canvas.bind("<Motion>", "motion") 
flag_on = False
# イベントループ --- (*4)
while True:
    event, values = window.read()
    print("#event=", event, values)
    if event in (sg.WINDOW_CLOSED, "閉じる"):
        break
    # キャンバス上でのマウスイベントを処理 --- (*5)
    if event == "-canvas-b_press": # ボタン押した時
        flag_on = True
    elif event == "-canvas-b_release": # ボタン離した時
        flag_on = False
    elif event == "-canvas-motion": # マウス移動した時
        if not flag_on:
            continue
        # マウスイベントを取得 --- (*6)
        e = canvas.user_bind_event
        x, y = e.x, e.y # マウスの位置を取り出す
        # 円を描く --- (*7)
        canvas.tk_canvas.create_oval(x, y, x+10, y+10, fill="white")
    # 画像を保存 --- (*8)
    elif event == "保存":
        x1 = canvas.tk_canvas.winfo_rootx()
        y1 = canvas.tk_canvas.winfo_rooty()
        x2 = x1 + canvas.tk_canvas.winfo_width()
        y2 = y1 + canvas.tk_canvas.winfo_height()
        image = ImageGrab.grab((x1, y1, x2, y2))
        image.save("paint.png")
        sg.popup("保存しました")
window.close()
