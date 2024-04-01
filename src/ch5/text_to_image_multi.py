import os
import io
from datetime import datetime
import platform
from queue import Queue
from threading import Thread
from PIL import Image
import PySimpleGUI as sg
# import TkEasyGUI as sg
from text_to_image import text_to_image

# 画像を保存する一時ディレクトリを用意する --- (*1)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DIR = os.path.join(SCRIPT_DIR, "tmp")
os.makedirs(TMP_DIR, exist_ok=True)
# UIイベントを管理するキュー
ui_events = Queue()

# ウィンドウを表示する関数
def show_window():
    image_loaded = 0
    # ウィンドウを作成する --- (*2)
    image_size=(300, 300)
    window = sg.Window("画像生成ツール", layout=[
        [sg.Text("生成したい画像の説明を入力してください。", key="-info-")],
        [sg.Multiline(size=(60, 5), key="-prompt-"), sg.Button("生成")],
        [sg.Image(key="-image0-", size=image_size), sg.Image(key="-image1-", size=image_size)],
        [sg.Image(key="-image2-", size=image_size), sg.Image(key="-image3-", size=image_size)],
        [sg.Button("保存フォルダを開く")]
    ], font=("Helvetica", 14))
    # イベントループ
    while True:
        event, values = window.read(timeout=100, timeout_key="-TIMEOUT-")
        if event == sg.WIN_CLOSED:
            break
        # 生成ボタンが押された時の処理 --- (*3)
        if event == "生成":
            prompt = values["-prompt-"]
            if prompt == "":
                continue
            # 4枚いっぺんにスレッドを作成する --- (*4)
            image_loaded = 0
            for no in range(4):
                Thread(target=task_gen_image, args=(prompt, no)).start()
            window["生成"].update(disabled=True)
            window["-info-"].update("画像を生成中...")
        # 保存フォルダを開く(OSによって処理を変える) --- (*5)
        if event == "保存フォルダを開く":
            pf = platform.system() # プラットフォーム名を取得
            print("Platform=", pf)
            if pf == "Windows": # Windowsの場合
                os.system("start " + TMP_DIR)
            elif pf == "Darwin": # Macの場合
                os.system("open " + TMP_DIR)
        if event == "-TIMEOUT-":
            if not ui_events.empty():
                # 生成終了イベントを確認 --- (*6)
                ui_event, values = ui_events.get()
                if ui_event == "done":
                    # 画像を表示
                    no, image_path = values
                    img = Image.open(image_path).resize(image_size)
                    window[f"-image{no}-"].update(data=convert_png(img))
                    image_loaded += 1
                    if image_loaded >= 4:
                        window["生成"].update(disabled=False)
                        window["-info-"].update("画像を生成しました。")

# 画像を生成する関数を定義 --- (*7)
def task_gen_image(text, no):
    # 現在時刻を元にして画像ファイル名を決める
    cur_dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = os.path.join(TMP_DIR, f"{cur_dt}_{no}.png")
    text_to_image(path, text, quality="hd")
    # イベントをキューに追加する
    ui_events.put(("done", (no, path)))

# 画像をPNGバイナリに変換
def convert_png(image):
    bin = io.BytesIO()
    image.save(bin, format="PNG")
    return bin.getvalue()

if __name__ == "__main__":
    show_window()
