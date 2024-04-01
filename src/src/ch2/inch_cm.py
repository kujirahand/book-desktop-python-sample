import PySimpleGUI as sg

# ユーザーに値を尋ねる --- (*1)
inch_str = sg.popup_get_text(
    "インチからセンチへ変換します。何インチですか？")
if inch_str == "" or inch_str is None:
    sg.popup("何も入力されていません。")
    quit()
# 数値に変換してインチからセンチへ変換 --- (*2)
try:
    inch_val = float(inch_str)
except ValueError:
    inch_val = 0
cm_val = inch_val * 2.54
# 答えを表示 --- (*3)
sg.popup(f"答えは{cm_val}センチです。")
