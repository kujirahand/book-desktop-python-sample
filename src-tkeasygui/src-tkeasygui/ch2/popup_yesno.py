import TkEasyGUI as sg
# YesかNoを選択するダイアログを表示する --- (*1)
result = sg.popup_yes_no("ネコが好きですか？")
# 結果に応じたメッセージを表示 --- (*2)
if result == "Yes":
    sg.popup("ネコが好きなんですね！")
elif result == "No":
    sg.popup("ネコが好きでは無いんですね。")

