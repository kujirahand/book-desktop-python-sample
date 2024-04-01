from gui_test import show_window, sg
data = [
    ["果物の名前", "値段", "色"],
    ["リンゴ", 100, "赤色"],
    ["バナナ", 200, "黄色"],
    ["ミカン", 300, "橙色"]
]
show_window(layout=[
    [sg.Text("よくある果物と参考価格と色の表")],
    [sg.Table(
        values=data[1:],
        headings=data[0],
        auto_size_columns=True,
        expand_x=True,
    )],
    [sg.Button("終了")] 
], font=("", 14))
