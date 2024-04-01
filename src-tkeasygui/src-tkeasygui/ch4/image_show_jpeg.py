import os
import io
from PIL import Image
import TkEasyGUI as sg

# JPEG画像のパスを指定 --- (*1)
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'fuji.jpeg')
# 画像をPNG形式に変換する関数を定義 --- (*2)
def convert_png(image_path, size=(600, 600)):
    # 画像を開く
    img = Image.open(image_path)
    img.thumbnail(size=size) # 画像サイズをリサイズ
    # 画像をPNG形式に変換
    png = io.BytesIO()
    img.save(png, format="PNG")
    return png.getvalue()
# ウィンドウを作成 --- (*3)
window = sg.Window(
    'JPEG画像の表示',
    layout=[
        [sg.Image(convert_png(image_path))],
        [sg.Button('閉じる')]
    ])
# イベントループ --- (*4)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "閉じる":
        break
window.close()
