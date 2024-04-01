from gui_test import show_window, sg
show_window(layout=[
    [sg.Text("好きな食べ物を選んでください(複数選択可)")],
    [sg.Checkbox(s,key=s) for s in ["リンゴ", "バナナ", "ミカン"]],
    [sg.Text("いつ食べますか？")],
    [sg.Combo(["朝ご飯", "昼ご飯", "夜ご飯"], key="-combo-")],
    [sg.Button("終了")] 
], font=("", 14))
