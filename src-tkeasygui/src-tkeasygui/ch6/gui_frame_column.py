from gui_test import show_window, sg
# 左右のカラムを定義
left_column = [[sg.Text("左側のテキスト")],[sg.Button("左側のボタン")]]
right_column = [[sg.Text("右側のテキスト")],[sg.Button("右側のボタン")]]
# フレームに左右のカラムを配置
frame_layout = [[
    sg.Column(left_column),
    sg.VSeparator(),
    sg.Column(right_column)
]]
# ウィンドウを表示
show_window(layout=[
    [sg.Frame("フレーム内に左右のカラムを配置", layout=frame_layout)],
    [sg.Button("終了")] 
], font=("", 14))
