import os, io
from threading import Thread
from queue import Queue
import urllib.parse
from PIL import Image
import TkEasyGUI as sg
from selenium import webdriver

# スクリプトのあるディレクトリを取得
SCRIPT_DIR = os.path.dirname(__file__)
# 並列処理の終了待ちキュー
ui_events = Queue()

# ウィンドウを作成する関数
def show_widnow():
    # ウィンドウの作成 --- (*1)
    layout = [
        [sg.Text('検索ワードを入力してください')],
        [sg.InputText(key='-keyword-')],
        [sg.Button('検索'), sg.Button('終了')],
        [sg.Image(key="-image-")]
    ]
    window = sg.Window('画像検索', layout)
    # イベントループ
    while True:
        event, values = window.read(timeout=100, timeout_key="-timeout-")
        if event in [sg.WIN_CLOSED, '終了']:
            break
        # 検索ボタンが押された時の処理 --- (*2)
        if event == '検索':
            keyword = values['-keyword-']
            Thread(target=search_image, args=(keyword,)).start()
            continue
        # タイムアウト時の処理 --- (*3)
        if event == "-timeout-":
            if ui_events.empty():
                continue
            # 画像検索の結果を受け取る --- (*4)
            event, values = ui_events.get()
            if event == 'update_image':
                window['-image-'].update(
                    data=load_image(values["path"]),
                    size=(500, 400))
    window.close()

# ブラウザを起動して画像検索を行う関数 --- (*5)
def search_image(keyword):
    # キーワードをURLエンコード --- (*6)
    key_enc = urllib.parse.quote(keyword)
    # Chromeを起動 --- (*7)
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 800)
    # 画像検索のページにアクセス --- (*8)
    url = f"https://google.com/search?q={key_enc}&sclient=img&tbm=isch"
    driver.get(url)
    driver.implicitly_wait(10) # 読み込み完了まで最大10秒待つ
    # スクリーンショットを撮影 --- (*9)
    savefile = os.path.join(SCRIPT_DIR, f"shot-{key_enc}.png")
    driver.save_screenshot(savefile)
    driver.quit() # ブラウザを終了 --- (*10)
    ui_events.put(('update_image', {"path": savefile}))

def load_image(path):
    # 画像を読んでリサイズしてバイナリデータを返す --- (*11)
    im = Image.open(path)
    im.thumbnail((500, 400))
    bio = io.BytesIO()
    im.save(bio, format="PNG")
    return bio.getvalue()

if __name__ == "__main__":
    show_widnow()
