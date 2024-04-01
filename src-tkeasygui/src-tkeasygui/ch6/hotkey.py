# ホットキーを設定するサンプルプログラム
import platform
import TkEasyGUI as sg
from queue import Queue
# macOSで実行したら未対応の旨を表示して終了
if platform.system() == "Darwin":
    sg.popup("macOSに対応していません")
    quit()
# イベント管理用の変数 --- (*1)
key_events = Queue()
# ホットキーを指定 --- (*2)
import keyboard
keyboard.add_hotkey("ctrl+q", lambda : key_events.put("exit"))
keyboard.add_hotkey("ctrl+a", lambda : key_events.put("show"))
# ウィンドウを作成 --- (*3)
def show_window():
    # 使い方を表示
    sg.popup("\n".join(["以下のホットキーを設定しました。",
        "Ctrl+q ... プログラムを終了します。",
        "Ctrl+a ... ことわざを表示します。"]))
    # ウィンドウを最小化で起動 --- (*4)
    window = sg.Window("Hotkey", layout=[[
        sg.Text("ホットキーを設定しています。"), sg.Button("終了")]],
        finalize=True)
    window.minimize()
    # イベントループ
    while True:
        event, _ = window.read(timeout=10, timeout_key="-timeout-")
        if event in ["終了", sg.WIN_CLOSED]: # ループを抜ける
             break
        if event == "-timeout-":
            # ホットキーのイベントを処理 --- (*5)
            if key_events.empty():
                continue
            key = key_events.get()
            if key == "exit": # ループを抜ける --- (*6)
                break
            elif key == "show": # ことわざを表示 --- (*7)
                sg.popup("[Ctrl]+[a]が押されました。\n能ある鷹は爪を隠す")
    window.close()

if __name__ == "__main__":
    show_window()
