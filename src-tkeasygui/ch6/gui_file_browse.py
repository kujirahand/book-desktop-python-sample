from gui_test import show_window, sg
show_window(layout=[
    [sg.Text("ファイルを選択:")],
    [sg.Input(key="-file-"), sg.FileBrowse()],
    [sg.Text("フォルダを選択:")],
    [sg.Input(key="-folder-"), sg.FolderBrowse()],
    [sg.Button("終了")] 
], font=("", 14))
