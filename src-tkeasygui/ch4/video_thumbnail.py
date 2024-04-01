import TkEasyGUI as sg
import PIL.Image as Image
import io
import subprocess

# FFmpegのパスを指定 --- (*1)
FFMPEG_PATH = "ffmpeg"

# ウィンドウを表示する関数を定義 --- (*2)
def show_window():
    # 画面レイアウトを定義 --- (*3)
    layout = [
        [sg.Text('動画ファイルを指定:')],
        [
            sg.InputText(key="infile", enable_events=True),
            sg.FileBrowse()
        ],
        [sg.Image(key="image")],
        [sg.Text('サムネイル位置:')],
        [sg.InputText(key="time", default_text="00:00:03")],
        [sg.Button('サムネイル生成')]
    ]
    win = sg.Window('動画サムネイル生成', layout)
    # イベントループを記述 --- (*4)
    while True:
        event, values = win.read()
        if event == sg.WIN_CLOSED:
            break
        # 動画を選択したらサムネイルを抽出 --- (*5)
        if event == "infile" or event == "サムネイル生成":
            if not values["infile"]:
                continue
            bin = extract_thumb(values["infile"], values["time"])
            win["image"].update(data=bin)
    win.close()

# 動画ファイルからサムネイルを抽出する関数を定義 --- (*6)
def extract_thumb(video_path, time_str, size=(500, 500)):
    # サムネイルを生成 --- (*7)
    thumb_path = video_path.replace(".mp4", "") + "_thumb.png"
    subprocess.run([
        FFMPEG_PATH, "-y", "-i", video_path, 
        "-ss", time_str, "-vframes", "1", thumb_path
    ])
    # プレビュー用に画像を開く --- (*8)
    img = Image.open(thumb_path)
    img.thumbnail(size=size) # サムネイル作成
    png = io.BytesIO() # 画像をPNG形式に変換して返す
    img.save(png, format="PNG")
    return png.getvalue()

if __name__ == "__main__":
    show_window()
