import os, json
import TkEasyGUI as sg
from queue import Queue
from threading import Thread
import chatbot
import todo_ai_template

# 変数の宣言 --- (*1)
todo_items = [] # ToDOを管理するリスト
ui_que = Queue() # uiのイベントを管理するキュー
script_dir = os.path.dirname(os.path.abspath(__file__))
todo_file = os.path.join(script_dir, "todo.json") # 保存ファイル

# 自動的にファイルからToDOを読み込む --- (*2)
if os.path.exists(todo_file):
    with open(todo_file, "r", encoding="utf-8") as f:
        todo_items = json.load(f)

# ウィンドウを表示する関数 --- (*3)
def show_window():
    layout = [
        [sg.Text("ToDO:"), sg.Input(key="input"), sg.Button("追加")],
        [sg.Table(
            headings=["重要度", "タグ", "アイテム", "一言"],
            values=todo_items,
            auto_size_columns=False,
            # col_widths=[3, 3, 15, 25], # 列幅を指定
            expand_x=True, expand_y=True, justification='left',
            key="items")],
        [sg.Button("削除")]
    ]
    # ウィンドウを作成 --- (*4)
    win = sg.Window("AI搭載のToDoアプリ", layout, resizable=True,
            font=("Arial", 14), size=(640, 400))
    # イベントループ --- (*5)
    while True:
        event, values = win.read(timeout=100, timeout_key="タイムアウト")
        if event == sg.WIN_CLOSED: break
        elif event == "追加": add_item_handler(win, values)
        elif event == "削除": del_item_handler(win, values)
        elif event == "タイムアウト": idle_handler(win, values)
    win.close()

# 追加ボタンを押した時の処理 --- (*6)
def add_item_handler(win, values):
    user = values["input"].strip()
    if user == "": return
    # 暫定的にアイテムを追加
    todo_items.append([5, "?", user, "AI問い合わせ中..."])
    # AIにアイテムの判定を依頼
    Thread(target=add_item_thread, args=(user,)).start()
    win["input"].update("")
    win["items"].update(values=todo_items) # 暫定的な更新

# 削除ボタンを押した時の処理 --- (*7)
def del_item_handler(win, values):
    if values["items"]:
        index = values["items"][0]
        del todo_items[index]
        save_item(win)

# アイドル状態(何も仕事がない状態)になった時の処理 --- (*8)
def idle_handler(win, values):
    if ui_que.empty(): return
    # UIイベントの処理 --- (*9)
    ui_event, ui_values = ui_que.get_nowait()
    if ui_event == "update_items":
        save_item(win)

# AIを使ってタスク判定を行う関数 --- (*10)
def add_item_thread(user):
    # ChatGPTに与える最初のプロンプト
    chatbot.messages = [{"role": "system",
                        "content": "あなたは優秀な秘書です。"}]
    # プロンプトに入力を埋め込みChatGPTにアクセス --- (*11)
    prompt = todo_ai_template.ADD_ITEM.replace("__INPUT__", user)
    r = chat_json(prompt)
    # AIの実行結果をアイテムに反映する --- (*12)
    for i, item in enumerate(todo_items):
        if item[2] == user: # 暫定追加したアイテムを書き換える
            todo_items[i] = [r["重要度"], r["タグ"], user, r["一言"]]
    # 処理の完了をUIに通知
    ui_que.put_nowait(("update_items", {}))

# ChatGPTにアクセスし応答をJSONで受け取る関数 --- (*13)
def chat_json(user):
    res = chatbot.chat_chatgpt(user)
    print("応答: ", res)
    # JSONだけを抽出する
    if '```' in res:
        res = res.replace("```json", "```").split("```")[1]
    try:
        res = json.loads(res) # JSONをパース
    except:
        res = {"一言": "エラー", "重要度": 5, "タグ": "不明"}
    return res

# ファイルにToDOアイテムを保存 --- (*14)
def save_item(win):
    with open(todo_file, "w", encoding="utf-8") as f:
        json.dump(todo_items, f)
    # ウィンドウのテーブルを更新
    win["items"].update(values=todo_items)

if __name__ == "__main__":
    show_window()
