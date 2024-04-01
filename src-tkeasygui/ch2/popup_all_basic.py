import TkEasyGUI as sg

# メッセージをダイアログに表示する
sg.popup("[1] popup")
# OKボタンを持ったダイアログ
sg.popup_ok("[2] popup_ok")
# OK/Cancelボタンを持つダイアログ
print(sg.popup_ok_cancel("[3] popup_ok_cancel"))
# YES/Noボタンを持つダイアログ
print(sg.popup_yes_no("[4] popup_yes_no"))
# Cancelledボタンを持つダイアログ
sg.popup_cancel("[5] popup_cancel")
# Errorボタンを持つダイアログ
sg.popup_error("[6] popup_error")
