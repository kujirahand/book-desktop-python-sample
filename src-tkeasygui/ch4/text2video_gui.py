import os, io, re
from queue import Queue
from threading import Thread
from PIL import Image
from text2video import text2video

import TkEasyGUI as sg

# 並列処理でイベントデータを保持するキューを作成 --- (*1)
ui_que = Queue()
# ウィンドウを作成して表示する関数 --- (*2)
def show_window():
    layout = [ # ウィンドウに配置するGUIパーツを定義
        [sg.Text("静止画を指定:")],
        [sg.Input(key="infile", enable_events=True), sg.FileBrowse()],
        [sg.Image(key="image")],
        [sg.Text("音声にしたいテキストを入力:")],
        [sg.Multiline(key="text", size=(50, 5))],
        [sg.Text("動画の保存先を指定:")],
        [sg.Input(key="outfile"), sg.FileSaveAs()],
        [sg.Button("動画作成", key="generate"), sg.Button("終了")]
    ]
    win = sg.Window("テキストと静止画から動画生成", layout)
    # イベントハンドラを定義 ---- (*3)
    while True:
        # タイムアウトを指定しつつイベントを受け取る --- (*4)
        event, values = win.read(timeout=100, timeout_key="-TIMEOUT-")
        if event in (None, "終了"):
            break
        # 画像ファイルが選択された時 --- (*5)
        if event == "infile":
            infile = values["infile"]
            if infile == "" or not os.path.exists(infile):
                continue
            outfile = re.sub(r"\.(jpg|png)$", "", infile) + ".mp4"
            win["image"].update(data=load_image(infile))
            win["outfile"].update(outfile)
        # 動画作成ボタンが押された時 --- (*6)
        if event == "generate":
            win["generate"].update(disabled=True)
            job = Thread(target=do_text2video, args=(values,))
            job.start()
        # タイムアウトした時 --- (*7)
        if event == "-TIMEOUT-":
            try:
                ui_event, ui_data = ui_que.get_nowait()
            except:
                ui_event, ui_data = None, None
            # 動画が完成した時 --- (*8)
            if ui_event == "done":
                sg.popup("動画生成が完了しました")
                win["generate"].update(disabled=False)
    win.close()

# 動画作成の関数 --- (*9)
def do_text2video(values):
    text2video(values["text"], values["infile"], values["outfile"])
    ui_que.put(("done", None))

# 画像をPNG形式に変換してバイナリで返す関数
def load_image(image_path, size=(300, 300)):
    img = Image.open(image_path)
    img.thumbnail(size=size)
    # 画像をPNG形式に変換
    png = io.BytesIO()
    img.save(png, format="PNG")
    return png.getvalue()

if __name__ == "__main__":
    show_window()