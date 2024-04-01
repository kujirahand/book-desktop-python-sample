import TkEasyGUI as sg
import subprocess
# FFmpegのパスを指定 --- (*1)
FFMPEG_PATH = "ffmpeg"
# GUI画面を表示する関数を定義 --- (*2)
def show_gui():
    # GUIのレイアウトを定義 --- (*3)
    layout = [
        [sg.Text("入力:動画ファイルの指定")],
        [
            # テキストが変更された時、イベントが発生するようにする --- (*3a)
            sg.Input(key="infile", enable_events=True),
            sg.FileBrowse()
        ],
        [sg.Text("出力:音声ファイルの指定")],
        [sg.Input(key="outfile"), sg.FileSaveAs()],
        [sg.Button("実行"), sg.Button("終了")]
    ]
    win = sg.Window("動画から音声を抽出する", layout)
    # イベントループ --- (*4)
    while True:
        event, values = win.read()
        if event in (None, "終了"):
            break
        if event == "infile":
            # 入力ファイルが指定されたら出力ファイル名を設定 --- (*5)
            if values["infile"]:
                f = values["infile"].replace(".mp4", "") + ".mp3"
                win["outfile"].update(f)
        if event == "実行":
            # MP3の抽出を実行 --- (*6)
            extract_mp3(values["infile"], values["outfile"])
            sg.popup("処理が完了しました")
    win.close()

# MP3の抽出を行う関数を定義 --- (*7)
def extract_mp3(input_file, output_file):
    subprocess.run([
        FFMPEG_PATH, "-y", "-i", input_file,
        "-vn", "-acodec", "libmp3lame", "-ab", "320k",
        output_file])

if __name__ == "__main__":
    show_gui()
