import math
import io
import datetime
from PIL import Image # 画像を読み取るため
import TkEasyGUI as sg

"""
必要に応じてPillowをインストールしてください
$ python3 -m pip install Pillow
"""

# 時計の中心座標を指定 --- (*1)
CENTER_X = 200
CENTER_Y = 200
# 背景画像を読み込む
BACK_IMAGE = "./clock-back.jpg"
back_image = Image.open(BACK_IMAGE)
# 画像をバイナリ形式に変換する必要がある
img_bytes = io.BytesIO()
back_image.save(img_bytes, format='PNG')
img_bytes = img_bytes.getvalue()

# メイン関数の定義 --- (*2)
def main():
    # ウィンドウのレイアウト --- (*3)
    layout = [
        [sg.Graph(
            canvas_size=(CENTER_X*2, CENTER_Y*2), # キャンバスのサイズを指定
            graph_bottom_left=(0, CENTER_Y*2), # 左下 
            graph_top_right=(CENTER_X*2, 0), # 右上
            key='-canvas-', # 識別キーを指定
            background_color='white' # 背景色を指定
        )],
        [sg.Button('終了')]]
    # ウィンドウの作成 --- (*4)
    window = sg.Window('アナログ時計', layout)
    canvas = window['-canvas-'] # キャンバスを取得
    # イベントループ
    while True:
        # イベントを取得する --- (*5)
        event, _ = window.read(timeout=100)
        # 閉じるボタンが押されたら終了
        if event in [sg.WINDOW_CLOSED, '終了']:
            break
        # 現在時刻を取得して時計を描画 --- (*6)
        draw_clock(canvas, datetime.datetime.now())
        # 画面を更新 --- (*7)
        window.refresh()
    window.close()

# 時計の針の座標を計算する関数 --- (*8)
def calc_hand_coords(angle, rate):
    x = CENTER_X + CENTER_X * rate * math.cos(angle)
    y = CENTER_Y + CENTER_Y * rate * math.sin(angle)
    return x, y
# 時計の針を描画する関数 --- (*9)
def draw_hand(canvas, angle, rate, width, color):
    x, y = calc_hand_coords(angle, rate)
    canvas.draw_line(
        (CENTER_X, CENTER_Y), (x, y), width=width, color=color)

# 時計を描画する関数 --- (*10)
def draw_clock(canvas, draw_time: datetime.datetime):
    # 時分秒を得る --- (*11)
    h, m, s = draw_time.hour, draw_time.minute, draw_time.second
    h = h % 12 # 12時間表示にする
    # キャンバスをクリアして時計の外枠を描画 --- (*12)
    canvas.erase()
    canvas.draw_image(data=img_bytes, location=(0, 0))
    # widget.create_oval(10, 10, CENTER_X*2-10, CENTER_Y*2-10, width=2)
    # 時計の目盛りを描画 --- (*13)
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x1, y1 = calc_hand_coords(angle, 0.85)
        x2, y2 = calc_hand_coords(angle, 0.95)
        canvas.draw_line((x1, y1), (x2, y2), width=3, color='white')
    # 各針を描画 --- (*14)
    h_angle = math.radians((h / 12 + m / 60 / 12) * 360 - 90) # 時の針
    draw_hand(canvas, h_angle, 0.5, 20, 'black')
    min_angle = math.radians((m / 60) * 360 - 90) # 分の針
    draw_hand(canvas, min_angle, 0.7, 15, 'black')
    sec_angle = math.radians((s / 60) * 360 - 90) # 秒の針
    draw_hand(canvas, sec_angle, 0.9, 2, 'red')

# メイン関数を呼び出す --- (*15)
if __name__ == '__main__':
    main()
