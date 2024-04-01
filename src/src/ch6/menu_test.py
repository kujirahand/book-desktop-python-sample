import PySimpleGUI as sg
# import TkEasyGUI as sg
menu_def = [
    ["item1", ["item1-1", "item1-2", "item1-3"]],
    ["item2", ["item2-1", "item2-2", "item2-3"]],
    ["item3", ["item3-1", "item3-2", "item3-3"]],
]
window = sg.Window("メニューのテスト",
    layout=[[
        sg.Menu(menu_def),
        sg.Multiline(size=(40, 15), key="-editor-", font=("", 14))]])
# イベントループ
while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, "終了"]: # 閉じる
        break
window.close()
