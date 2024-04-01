# 3分タイマー
import datetime
import PySimpleGUI as sg
# import TkEasyGUI as sg
import pygame

# 全体の設定 --- (*1)
SOUND_FILE = "beep.mp3" # 音声ファイルを指定
TIMER_SEC = 3 * 60 # タイマーの時間(秒)を指定
# MP3を再生するための設定 --- (*2)
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)
# タイマーのレイアウトを指定 --- (*3)
layout = [
    [sg.Text("00:00:00", key="-output-", font=("Helvetica", 80))],
    [
        sg.Button("スタート", font=("Helvetica", 20)), 
        sg.Button("リセット", font=("Helvetica", 20))
    ]
]
# ウィンドウを作成する
window = sg.Window("3分タイマー", layout)
start_time = None # 開始時刻を記録する変数
# イベントループ
while True:
    # イベントを取得する --- (*4)
    event, _ = window.read(timeout=10)
    # 閉じるボタンが押されたら終了
    if event == sg.WINDOW_CLOSED:
        break
    # スタートボタンを押した時 --- (*5)
    if event == "スタート":
        # 開始時刻を記録
        start_time = datetime.datetime.now()
    # リセットボタンを押した時 --- (*6)
    if event == "リセット":
        start_time = None
        window["-output-"].update("00:00:00")
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        continue
    # タイマーが始まっていない時 --- (*7)
    if start_time is None:
        continue
    # 経過時間を計算 --- (*8)
    now = datetime.datetime.now()
    delta = now - start_time
    # 3分経過したら音声を再生 --- (*9)
    if delta.seconds >= TIMER_SEC:
        pygame.mixer.music.play()
        start_time = None
        window["-output-"].update("00:00:00")
        continue
    # 残り時間を表示 --- (*10)
    remain = TIMER_SEC - delta.seconds
    window["-output-"].update(
        "0" + str(datetime.timedelta(seconds=remain)))
window.close()
