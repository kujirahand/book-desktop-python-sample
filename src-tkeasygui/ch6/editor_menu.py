from datetime import datetime
import TkEasyGUI as sg

def show_window():
    # メニューを定義 --- (*1)
    menu_def = [
        ["ファイル", ["新規", "---", "開く", "保存", "---", "終了"]],
        ["挿入", ["時刻", "日付"]],
    ]
    # エディタ画面を作成 --- (*2)
    window = sg.Window("エディタ",
        layout=[[
            sg.Menu(menu_def),
            sg.Multiline(size=(40, 15), key="-editor-", font=("", 14))]])
    # イベントループ --- (*3)
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, "終了"]: # 閉じる
            break
        # メニューの処理 --- (*4)
        if event == "新規":
            if sg.popup_yes_no("現在の内容を破棄しますか?") == "Yes":
                window["-editor-"].update("")
        elif event == "開く":
            filename = sg.popup_get_file("ファイルを選択")
            if filename:
                with open(filename, "r", encoding="utf-8") as f:
                    window["-editor-"].update(f.read())
        elif event == "保存":
            filename = sg.popup_get_file("保存するファイルを選択", save_as=True)
            if filename:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(values["-editor-"])
        elif event == "時刻": # 末尾に時刻を挿入 --- (*5)
            now_s = datetime.now().strftime("%H:%M:%S")
            window["-editor-"].print(now_s)
        elif event == "日付": # 末尾に日付を挿入
            today_s = datetime.now().strftime("%Y年%m月%d日")
            window["-editor-"].print(today_s)
    window.close()

if __name__ == "__main__":
    show_window()
