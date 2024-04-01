import PySimpleGUI as sg
# import TkEasyGUI as sg
# とにかくコピー＆ペーストボタンを10個作成したもの
window = sg.Window("たくさんのボタン", layout=[[
    sg.Button("1"), sg.Button("2"), sg.Button("3"),
    sg.Button("4"), sg.Button("5"), sg.Button("6"),
    sg.Button("7"), sg.Button("8"), sg.Button("9"),
    sg.Button("10")
]])
while True: # イベントループ
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED: break
window.close()