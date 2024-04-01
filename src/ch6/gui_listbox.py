from gui_test import show_window, sg
show_window(layout=[
    [sg.Text("好きな果物を選んでください")],
    [sg.Listbox(
        ["リンゴ", "バナナ", "ミカン", "イチゴ", "メロン"],
        key="-list-", size=(10, 5))],
    [sg.Button("終了")] 
], font=("", 14))
