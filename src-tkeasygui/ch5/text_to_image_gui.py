import io
from queue import Queue
from threading import Thread
from PIL import Image
import TkEasyGUI as sg
from text_to_image import text_to_image

# 画像を保存する一時ファイル名
TEMP_IMAGE_FILE = "text_to_image_test.png"
# UIイベントを管理するキュー
ui_events = Queue()

# ウィンドウを表示する関数
def show_window():
    # ウィンドウを作成する --- (*1)
    window = sg.Window("画像生成ツール", layout=[
        [sg.Text("生成したい画像の説明を入力してください。", key="-info-")],
        [sg.Multiline(size=(60, 5), key="-prompt-"), sg.Button("生成")],
        [sg.Image(key="-image-", size=(500, 500))]
    ], font=("Helvetica", 14))
    # イベントループ --- (*2)
    while True:
        event, values = window.read(timeout=100, timeout_key="-TIMEOUT-")
        if event == sg.WIN_CLOSED:
            break
        # 生成ボタンが押された時の処理 --- (*3)
        if event == "生成":
            prompt = values["-prompt-"]
            if prompt == "":
                continue
            Thread(target=task_gen_image, args=(prompt,)).start()
            window["生成"].update(disabled=True)
            window["-info-"].update("画像を生成中...")
        if event == "-TIMEOUT-":
            if not ui_events.empty():
                # 生成終了イベントを確認 --- (*4)
                ui_event = ui_events.get()
                if ui_event == "done":
                    # 画像を表示
                    img = Image.open(TEMP_IMAGE_FILE)
                    img = img.resize((500, 500))
                    window["-image-"].update(data=convert_png(img))
                    window["生成"].update(disabled=False)
                    window["-info-"].update("画像を生成しました。")

# 画像を生成する関数を定義 --- (*5)
def task_gen_image(text):
    # 画像を生成
    text_to_image(TEMP_IMAGE_FILE, text, quality="hd")
    # イベントをキューに追加する
    ui_events.put("done")

# 画像をPNGバイナリに変換
def convert_png(image):
    bin = io.BytesIO()
    image.save(bin, format="PNG")
    return bin.getvalue()

if __name__ == "__main__":
    show_window()
