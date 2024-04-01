import io
from PIL import Image
import TkEasyGUI as sg
import pyperclip
import easyocr

# ウィンドウを表示する関数を定義 --- (*1)
def show_window():
    # レイアウトを作成 --- (*2)
    layout = [
        [sg.Text("画像ファイルを選択してください")],
        [sg.Input(key="infile", enable_events=True), sg.FileBrowse()],
        [ # 左側に画像、右側にOCR結果表示用エディタ --- (*2a)
            sg.Image(key="image", size=(300, 200)),
            sg.Multiline(key="result", size=(50, 20))
        ],
        [sg.Button("OCR実行",key="ocr_exec"), sg.Button("終了")]
    ]
    # ウィンドウを作成 --- (*3)
    win = sg.Window("画像OCRクリップボード", layout)
    # イベントループ --- (*4)
    while True:
        event, values = win.read()
        if event in (None, "終了"):
            break
        # 画像ファイルを選択した時 --- (*5)
        if event == "infile":
            win["image"].update(load_image(values["infile"]))
        # OCR実行ボタンを押した時 --- (*6)
        elif event == "ocr_exec":
            # OCR実行
            text = ocr_image(values["infile"], win)
            win["result"].update(text)
            pyperclip.copy(text)
            sg.popup("OCR結果をクリップボードにコピーしました")
 
def ocr_image(image_path, win):
    # EasyOCRのオブジェクトを作成して読み取る --- (*7)
    reader = easyocr.Reader(["ja", "en"])
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)

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
