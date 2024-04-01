import os, io, time
from threading import Thread
from queue import Queue
from PIL import Image
import PySimpleGUI as sg
# import TkEasyGUI as sg
from selenium import webdriver

# 巡回表示したいURLとスクロール量を指定 --- (*1)
URL_VIEWS = [
    # 気象庁の天気予報
    ("https://www.jma.go.jp/bosai/map.html#5/34.5/137/&contents=forecast", 0),
    # 日経平均株価
    ("https://finance.yahoo.co.jp/quote/998407.O/chart", 400),
    # 円ドル為替
    ("https://finance.yahoo.co.jp/quote/USDJPY=FX", 500),
    # 交通情報
    ("https://www.drivetraffic.jp/", 0)
]
SCRIPT_DIR = os.path.dirname(__file__) # スクリプトパス
IMAGE_SIZE = (500,400) # 1画面のサイズ
APP_TITLE = "Webサイトを定期的にスクリーンショット"
ui_events = Queue() # 並列処理の終了待ちキュー

# ウィンドウを作成する関数
def show_widnow():
    # ウィンドウの作成 --- (*2)
    layout = [
        [sg.Button('終了'), sg.Text("定期的に画面を更新します")],
        [sg.Image(key="-image0-", size=IMAGE_SIZE),
         sg.Image(key="-image1-", size=IMAGE_SIZE)],
        [sg.Image(key="-image2-", size=IMAGE_SIZE),
         sg.Image(key="-image3-", size=IMAGE_SIZE)]
    ]
    window = sg.Window(APP_TITLE, layout)
    # ブラウザ画面の更新処理 --- (*3)
    update_screen(wait=5)
    # イベントループ --- (*4)
    update_timer = 0
    while True:
        event, values = window.read(timeout=100, timeout_key="-timeout-")
        if event in [sg.WIN_CLOSED, '終了']: # 終了ボタンが押された時
            break
        # タイムアウト時の処理 --- (*5)
        if event == "-timeout-":
            if not ui_events.empty():
                # スクリーンショット保存の結果を受け取る --- (*5a)
                event, values = ui_events.get()
                if event == "image_update":
                    im, no = values["data"], values["no"]
                    window[f"-image{no}-"].update(data=im)
                    continue
            # 画面を自動更新するか確認 --- (*5b)
            update_timer += 100
            window.set_title(f"{APP_TITLE}-{60000-update_timer:05}")
            if update_timer > 60000:
                update_screen(wait=10)
                update_timer = 0

    window.close()

# ブラウザ画面を連続で更新処理する --- (*6)
def update_screen(wait=2):
    for no, url_scr in enumerate(URL_VIEWS):
        print(no, url_scr)
        Thread(target=screen_shot, args=(url_scr, no, wait)).start()

# ブラウザを起動してスクリーンショットを保存 --- (*7)
def screen_shot(url_scr, no, wait):
    # Chromeをヘッドレスで起動 --- (*8)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1024, 800)
    # ページにアクセス --- (*9)
    driver.get(url_scr[0])
    driver.implicitly_wait(10)
    time.sleep(wait) # 待ち時間を指定
    # 画面をスクロール --- (*10)
    driver.execute_script(f"window.scrollTo(0, {url_scr[1]});")
    # スクリーンショットを撮影 --- (*11)
    savefile = os.path.join(SCRIPT_DIR, f"shot-{no}.png")
    driver.save_screenshot(savefile)
    driver.quit() # ブラウザを終了
    im = load_image(savefile) # 画像を読み込む
    # イベントキューに「image_update」を追加 --- (*12)
    ui_events.put(("image_update", {"data": im, "no": no}))

def load_image(path):
    # 画像を読んでリサイズしてバイナリデータを返す --- (*13)
    im = Image.open(path)
    im.thumbnail(IMAGE_SIZE)
    bio = io.BytesIO()
    im.save(bio, format="PNG")
    return bio.getvalue()

if __name__ == "__main__":
    show_widnow()
