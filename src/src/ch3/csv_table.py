import PySimpleGUI as sg
# import TkEasyGUI as sg
import csv

# CSVファイルを読み込む --- (*1)
with open("fruits.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# レイアウトを定義 --- (*2)
layout = [
    [sg.Table(
        values=data[1:], # テーブルに表示するデータ(ヘッダ行を含まない)を指定
        headings=data[0], # ヘッダ行を指定
        expand_x=True, # ウィンドウのX方向にサイズを合わせる
        expand_y=True, # ウィンドウのY方向にサイズを合わせる
        justification='center', # セルを中央揃えにする
        auto_size_columns=True, # 自動的にカラムを大きくする
        max_col_width=30, # 最大カラムサイズを指定
        font=("Arial", 14))]
]
# ウィンドウを作成 --- (*3)
windows = sg.Window("CSVビューア", layout,
                    size=(500, 300),
                    resizable=True, finalize=True)
# イベントループ --- (*4)
while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED:
        break
windows.close()
