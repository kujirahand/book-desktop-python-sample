import TkEasyGUI as sg # ← この一行を書き換えただけ

# ユーザーに値を尋ねる
inch_str = sg.popup_get_text(
    "インチからセンチへ変換します。何インチですか？")
if inch_str == "" or inch_str is None:
    sg.popup("何も入力されていません。")
    quit()
# 数値に変換してインチからセンチへ変換
try:
    inch_val = float(inch_str)
except ValueError:
    inch_val = 0
cm_val = inch_val * 2.54
# 答えを表示
sg.popup(f"答えは{cm_val}センチです。")
