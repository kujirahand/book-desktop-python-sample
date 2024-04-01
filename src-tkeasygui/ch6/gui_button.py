from gui_test import show_window, sg
show_window(layout=[
    [sg.Button(s) for s in ["リンゴ", "バナナ", "ミカン"]],
    [sg.Button("終了"), sg.Button("テスト", key="-test-")]
])
