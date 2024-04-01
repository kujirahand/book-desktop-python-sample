import io
from queue import Queue
from threading import Thread
from PIL import Image
import pyperclip
import easyocr
import TkEasyGUI as sg

# 並列処理でイベントデータを保持するキューを作成 --- (*1)
ui_que = Queue()

# ウィンドウを表示する関数を定義
def show_window():
    layout = [
        [sg.Text('画像ファイルを選択してください')],
        [sg.Input(key='infile', enable_events=True), sg.FileBrowse()],
        [
            sg.Image(key='image'),
            sg.Multiline(key='result', size=(50, 20))
        ],
        [sg.Button('OCR実行',key="ocr_exec"), sg.Button('終了')]
    ]
    win = sg.Window('画像OCRクリップボード', layout)
    # イベントループ
    while True:
        # イベントループが処理がブロックしないようタイムアウトを指定 --- (*2)
        event, values = win.read(timeout=100, timeout_key="-TIMEOUT-")
        if event in (None, '終了'):
            break
        # ファイルを選択した時 --- (*3)
        if event == "infile":
            image_job = Thread(target=load_image, args=(values['infile'],))
            image_job.start()
            ocr_thread_start(values['infile'], win)
        # OCR実行ボタンを押した時 --- (*4)
        elif event == 'ocr_exec':
            ocr_thread_start(values['infile'], win)
        # タイムアウトした時 --- (*5)
        elif event == '-TIMEOUT-':
            # キューからイベントを取得してUIを更新 --- (*6)
            try:
                ui_event, ui_data = ui_que.get_nowait()
            except:
                ui_event, ui_data = None, None
            # 画像の読み込みが完了した時 --- (*7)
            if ui_event == "image_loaded":
                win["image"].update(data=ui_data)
            # OCR処理が完了した時 --- (*8)
            elif ui_event == "ocr_done":
                # OCR実行ボタンが押せるように変更
                win["ocr_exec"].update(disabled=False)
                # 結果をテキストボックスに表示
                win["result"].update(ui_data)
                # 結果をクリップボードにコピー
                pyperclip.copy(ui_data)
                sg.popup_notify("OCR結果をクリップボードにコピーしました")

# OCR処理をスレッドで開始する --- (*9)
def ocr_thread_start(image_path, win):
    # OCR処理を実行するスレッドを作成
    win["result"].update("現在OCR処理中です...")
    # OCR実行ボタンを連続で押せないようにロック
    win["ocr_exec"].update(disabled=True)
    # OCR処理を実行
    ocr_job = Thread(target=ocr_image, args=(image_path,))
    ocr_job.start()

# OCR処理を実行する関数 --- (*10)
def ocr_image(image_path):
    # EasyOCRのオブジェクトを作成して読み取る
    reader = easyocr.Reader(["ja", "en"])
    result = reader.readtext(image_path, detail=0)
    text = "\n".join(result)
    ui_que.put(("ocr_done", text))

# 並列処理で利用して、画像を読み込む関数 --- (*11)
def load_image(image_path):
    # 画像をバイナリで読み取る
    img = Image.open(image_path)
    img.thumbnail(size=(300, 300))
    png = io.BytesIO()
    img.save(png, format="PNG")
    ui_que.put(("image_loaded", png.getvalue()))

if __name__ == "__main__":
    show_window()
