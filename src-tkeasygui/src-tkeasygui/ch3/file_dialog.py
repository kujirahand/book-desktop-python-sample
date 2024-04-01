import TkEasyGUI as sg

# ファイルの選択ダイアログ --- (*1)
file = sg.popup_get_file(
    "CSVファイルを1つ選択", 
    multiple_files=False, # ファイルを1つ選ぶ
    no_window=True,
    file_types=(("CSVファイル", "*.csv"),)
)
sg.popup(file, title="選択したファイル")

# 複数ファイルの選択ダイアログ --- (*2)
files = sg.popup_get_file(
    "CSVファイルを複数選択", 
    multiple_files=True, # 複数のファイルを選択
    no_window=True,
    file_types=(("CSVファイル", "*.csv"),)
)
sg.popup("\n".join(files), title="選択したファイル一覧")

# 保存用のファイル選択ダイアログ --- (*3)
file = sg.popup_get_file(
    "保存先のCSVファイルを指定", 
    save_as=True, # 保存用のダイアログ
    no_window=True,
    file_types=(("CSVファイル", "*.csv"),)
)
sg.popup(file, title="保存用に選択したファイル")
