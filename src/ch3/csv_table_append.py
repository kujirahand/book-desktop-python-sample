import csv
import PySimpleGUI as sg
# import TkEasyGUI as sg

def main():
    while True:
        # CSVファイルを選ぶ --- (*1)
        files = sg.popup_get_file(
            "複数のCSVファイルを選択", 
            multiple_files=True, # 複数のファイルを選ぶ
            no_window=True,
            file_types=(("CSVファイル", "*.csv"),)
        )
        if len(files) == 0 or files == "":
            break
        # 複数のCSVファイルをまとめる --- (*2)
        all_data = []
        for filename in files:
            data = read_csv(filename) # CSVファイルを読む
            if data is None:
                sg.popup_error(filename + "が読み込めません。")
                continue
            # もしヘッダ行が同じなら省略する --- (*3)
            if len(all_data) >= 2 and len(data) >= 2:
                if all_data[0] == data[0]:
                    data = data[1:]
            all_data += data
        # 結合したデータをテーブルに表示する --- (*4)
        if show_csv(all_data) == False:
            break

# CSVファイルを読む - UTF-8/Shift_JIS(CP932)対応版 --- (*5)
def read_csv(filename):
    encodings = ["UTF-8", "CP932", "EUC-JP"]
    for enc in encodings:
        try:
            with open(filename, "r", encoding=enc) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            return data
        except:
            pass
    return None

# CSVをテーブルに表示する --- (*6)
def show_csv(data):
    if len(data) == 0:
        data = [["空"], ["空"]]
    # レイアウトを定義 --- (*7)
    layout = [
        [sg.Table(
            key="-table-",
            values=data[1:], # データ
            headings=data[0], # ヘッダ
            expand_x=True, expand_y=True, # ウィンドウに合わせる
            justification='left', # セルを左揃えにする
            auto_size_columns=True, # 自動的にカラムを大きくする
            max_col_width=30, # 最大カラムサイズを指定
            font=("Arial", 14))],
        [sg.Button('ファイル選択'), sg.Button('保存'), sg.Button('終了')]
    ]
    # ウィンドウを作成 --- (*8)
    window = sg.Window("CSVビューア", layout,
                size=(500, 300), resizable=True, finalize=True)
    # イベントループ
    flag_continue = False
    while True:
        event, _ = window.read()
        if event in [sg.WIN_CLOSED, "終了"]:
            break
        # ファイル追加ボタンを押したとき
        if event == "ファイル選択":
            flag_continue = True
            break
        # 保存ボタンを押したとき
        if event == "保存":
            # ファイルを選ぶ --- (*9)
            filename = sg.popup_get_file(
                "保存するCSVファイルを選択",
                save_as=True,
                no_window=True,
                file_types=(("CSVファイル", "*.csv"),)
            )
            if filename == "" or filename is None:
                continue
            # CSVファイルに書き込む --- (*10)
            with open(filename, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
    window.close()
    return flag_continue

if __name__ == "__main__":
    main()
