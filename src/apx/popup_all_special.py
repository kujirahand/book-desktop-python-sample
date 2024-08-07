import PySimpleGUI as sg
# import TkEasyGUI as sg

# 待ち時間のないダイアログ --- (*7)
sg.popup_no_wait("[7] popup_no_wait")
# 3秒で自動的に閉じる --- (*8)
print(sg.popup_auto_close("[8] popup_auto_close", auto_close_duration=3))
# ボタンのないダイアログ --- (+9)
sg.popup_no_buttons("[9] popup_no_buttons")
# テキスト入力ダイアログ --- (*10)
sg.popup_get_text("[10] popup_get_text")
# 通知領域に情報を表示する --- (*11)
sg.popup_notify("[11] popup_notify")
# ファイル選択ダイアログ --- (*12)
sg.popup_get_file("[12] popup_get_file")
# フォルダ選択ダイアログ --- (*13)
sg.popup_get_folder("[13] popup_get_folder")
# 複数行入力ボックス --- (*14)
print(sg.popup_scrolled("[14] popup_scrolled\n複数行\n入力"))
# 日付入力ボックス --- (*15)
print(sg.popup_get_date(title="[15] popup_get_date"))

