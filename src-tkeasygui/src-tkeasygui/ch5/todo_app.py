import os
import json
import TkEasyGUI as sg

# 保存ファイルの指定 --- (*1)
script_dir = os.path.dirname(os.path.abspath(__file__))
todo_file = os.path.join(script_dir, "todo.json") # 保存ファイル
# ToDOを管理するリスト --- (*2)
todo_items = [[5, "買い物", "牛乳を買う", "毎朝飲みますね"]]
# 既に保存ファイルがあれば自動的にファイルから読む --- (*3)
if os.path.exists(todo_file):
    with open(todo_file, "r", encoding="utf-8") as f:
        todo_items = json.load(f)
# ウィンドウを表示する関数 --- (*4)
def show_window():
    layout = [
        # 「ToDO追加」のフレーム --- (*5)
        [sg.Frame(title="ToDo追加", layout=[
            [sg.Text("ToDO:", size=(7,1)),
                sg.Input(key="input")],
            [sg.Text("重要度:", size=(7,1)),
                sg.Input(key="level", default_text="5")],
            [sg.Text("タグ:", size=(7,1)),
                sg.Input(key="tag")],
            [sg.Text("一言:", size=(7,1)),
                sg.Input(key="comment")],
            [sg.Button("追加")]
        ])],
        # アイテム表示用のテーブル --- (*6)
        [sg.Table(
            headings=["重要度", "タグ", "アイテム", "一言"], # ヘッダ列
            values=todo_items, # 表示するデータ
            expand_x=True, expand_y=True,
            auto_size_columns=True,
            justification='left',
            key="items")],
        [sg.Button("削除")]
    ]
    win = sg.Window("ToDoアプリ", layout, font=("Arial", 14), size=(600, 400))
    # イベントループ --- (*7)
    while True:
        event, values = win.read(timeout=10, timeout_key="-TIMEOUT-")
        if event == sg.WIN_CLOSED:
            break
        if event == "追加": # 追加ボタンを押した時の処理 --- (*8)
            todo_items.append([
                values["level"],
                values["tag"],
                values["input"],
                values["comment"]
            ])
            win["input"].update("")
            win["comment"].update("")
            save_item(win)
        if event == "削除": # 削除ボタンを押した時の処理 --- (*9)
            if values["items"]:
                index = values["items"][0]
                del todo_items[index]
                save_item(win)
    win.close()
# ファイルにToDOアイテムを保存 --- (*10)
def save_item(win):
    with open(todo_file, "w", encoding="utf-8") as f:
        json.dump(todo_items, f)
    # ウィンドウのテーブルを更新
    win["items"].update(values=todo_items)

if __name__ == "__main__":
    show_window()
