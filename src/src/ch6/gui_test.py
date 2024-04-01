import PySimpleGUI as sg
# import TkEasyGUI as sg
def show_window(layout, after_create=None, font=None):
    window = sg.Window("GUIのテスト", layout, font=font,finalize=True)
    if after_create is not None: after_create(window)
    while True:
        event, values = window.read()
        print(event, values)
        if event in [sg.WIN_CLOSED, "終了"]: # 閉じる
            break
    window.close()
