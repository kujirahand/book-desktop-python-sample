import PySimpleGUI as sg
# import TkEasyGUI as sg
from queue import Queue
from threading import Thread
import chatbot
import memo_ai_template

# 変数の宣言 --- (*1)
# テンプレートで定義したプロンプトの名前一覧を得る
ai_functions = memo_ai_template.TEMPLATES.keys()
ui_que = Queue() # uiのイベントを管理するキュー
# ウィンドウを表示する関数 --- (*2)
def show_window():
    # 画面上部のボタンを動的に生成 --- (*3)
    file_buttons = [[sg.Button(n) for n in ["読込", "保存"]]]
    ai_buttons = [[sg.Button(n, key=n) for n in ai_functions]]
    # レイアウトの定義
    layout = [
        [sg.Frame("ファイル", layout=file_buttons),
         sg.Frame("AI機能", layout=ai_buttons)],
        [sg.Multiline(key="editor", expand_x=True, expand_y=True)],
        [sg.Text("AIの応答:"), sg.Button("↑と↓を入れ替え")],
        [sg.Multiline(key="result", size=(40, 7), expand_x=True,
                      background_color="#e0f0f0")],
    ]
    # ウィンドウを作成 --- (*4)
    win = sg.Window("AI搭載のメモアプリ", layout, resizable=True,
            font=("Arial", 14), size=(600, 400))
    # イベントハンドラの定義 --- (*5)
    events = {
        "保存": save_handler,
        "読込": load_handler,
        "↑と↓を入れ替え": swap_editor_handler,
        "タイムアウト": idle_handler,
    }
    # AI機能のボタンにイベントハンドラを割り当てる --- (*6)
    for key in ai_functions:
        events[key] = ai_handler
    # イベントループ --- (*7)
    while True:
        event, values = win.read(timeout=100, timeout_key="タイムアウト")
        if event == sg.WIN_CLOSED: break
        # イベントハンドラがあればそれを呼び出す --- (*8)
        if event in events:
            events[event](event, win, values)
    win.close()

# 「保存」ボタンを押した時の処理 --- (*9)
def save_handler(event, win, values):
    file = sg.popup_get_file("保存するファイルを選択", save_as=True)
    if file == "" or file is None: return
    with open(file, "w", encoding="utf-8") as f:
        f.write(values["editor"])

# 「読込」ボタンを押した時の処理 --- (*10)
def load_handler(event, win, values):
    file = sg.popup_get_file("読込むファイルを選択", save_as=False)
    if file == "" or file is None: return
    with open(file, "r", encoding="utf-8") as f:
        win["editor"].update(f.read())

# AIボタンを押した時の処理 --- (*11)
def ai_handler(event, win, values):
    text = values["editor"].strip()
    win["result"].update("AIの応答を待っています...")
    # AIボタンを全てを押せないようにする --- (*12)
    for name in ai_functions:
        win[name].update(disabled=True)
    # AIに要約を依頼
    Thread(target=ai_task_thread, args=(event, text)).start()

# タスクを指定してChatGPT APIを呼び出す関数 --- (*13)
def ai_task_thread(task, text):
    # プロンプトのテンプレートを取得
    template = memo_ai_template.TEMPLATES[task]
    # プロンプトを構築 --- (*14)
    text = text.replace("`", "｀")
    prompt = template.replace("__INPUT__", text)
    # ChatGPTにアクセス --- (*15)
    res = chatbot.chat_chatgpt(prompt)
    ui_que.put(("result", {"result": res}))
    
# 「↑と↓を入れ替える」ボタンを押した時の処理 --- (*16)
def swap_editor_handler(event, win, values):
    win["editor"].update(values["result"])
    win["result"].update(values["editor"])

# アイドル状態(何も仕事がない状態)になった時の処理 --- (*17)
def idle_handler(event, win, values):
    if ui_que.empty(): return
    # UIイベントの処理 --- (*18)
    ui_event, ui_values = ui_que.get_nowait()
    if ui_event == "result":
        # エディタに結果を表示 --- (*19)
        win["result"].update(ui_values["result"])
        # AIボタンを全てを押せるように戻す
        for name in ai_functions:
            win[name].update(disabled=False)

if __name__ == "__main__":
    show_window()
