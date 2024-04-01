from gui_test import show_window, sg
show_window(layout=[
    [sg.Text("変更できないテキスト")],
    [sg.Input("ユーザーが入力できるテキスト", key="-input-")],
    [sg.Button("終了")]
])
