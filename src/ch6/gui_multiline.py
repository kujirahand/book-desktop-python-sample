from gui_test import show_window, sg
show_window(layout=[
    [sg.Multiline("複数行の\nテキストボックス",
        key="-multiline-", size=(40, 5))],
    [sg.Button("終了")] 
], font=("", 14))
