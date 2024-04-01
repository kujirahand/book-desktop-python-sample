import io
from PIL import Image, ImageEnhance, ImageFilter
import TkEasyGUI as sg

# メイン関数を定義 --- (*1)
def main():
    # 対象画像ファイルの選択
    fname = sg.popup_get_file("画像ファイルを選択してください", no_window=True)
    if not fname: exit()
    # 画像を表示してフィルタ処理を開始
    show_image_editor(fname)

# 画像エディタを表示する関数を定義 --- (*2)
def show_image_editor(image_path):
    # 画像を読み込む
    raw_img = Image.open(image_path)
    def_image = raw_img.resize((400, 400))
    # レイアウト左側を定義(画像表示) --- (*3)
    col_left = [
        [sg.Image(convert_png(def_image), key="image")]]
    # レイアウト右側を定義(複数のスライダーを表示) --- (*4)
    col_right = [
        [sg.Text("コントラスト")],
        [sg.Slider(key="contrast",
            range=(0, 2), resolution=0.1, default_value=1,
            orientation="h", enable_events=True)
        ],
        [sg.Text("明るさ")],
        [sg.Slider(key="brightness",
            range=(0, 10), resolution=0.1, default_value=1,
            orientation="h", enable_events=True)
        ],
        [sg.Text("ぼかし")],
        [sg.Slider(key="blur",
            range=(0, 10), resolution=1, default_value=0,
            orientation="h", enable_events=True)
        ]]
    # ウィンドウを作成 --- (*5)
    window = sg.Window("画像の表示", layout=[
        [
            sg.Column(col_left),
            sg.Column(col_right, vertical_alignment="top")
        ],
        [sg.Button("保存"), sg.Button("閉じる")]
    ])
    # イベントループ --- (*6)
    while True:
        # イベントの読み込み
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "閉じる":
            break
        # スライダーを動かした時の処理 --- (*7)
        if event == "contrast" or \
            event == "brightness" or \
            event == "blur":
            # 現在の設定でフィルタをかける --- (*8)
            f_img = filter_png(raw_img, values)
            bin = convert_png(f_img)
            # 画像を更新
            window["image"].update(data=bin)
        if event == "保存":
            # ファイル選択 --- (*9)
            fname = sg.popup_get_file(
                "保存するファイル名を入力してください", 
                save_as=True, no_window=True)
            if not fname: continue
            # 画像を保存 --- (*10)
            img2 = filter_png(raw_img, values, False)
            img2.save(fname)
            sg.popup("保存しました")
    window.close()

# 画像にフィルタをかける関数を定義 --- (*11)
def filter_png(image, values, is_resize=True):
    # パラメータから値を取り出す
    contrast = values["contrast"]
    brightness = values["brightness"]
    blur = values["blur"]
    # フィルタ処理を行う
    if blur > 0:
        # ぼかし処理
        image = image.filter(ImageFilter.GaussianBlur(radius=blur))
    if is_resize:
        image = image.resize((400, 400)) # 画像サイズを変更
    # コントラストと明るさを変更
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image =  ImageEnhance.Brightness(image).enhance(brightness)
    return image

# 画像をPNG形式に変換 --- (*12)
def convert_png(image):
    bin = io.BytesIO()
    image.save(bin, format="PNG")
    return bin.getvalue()

if __name__ == "__main__":
    main()
