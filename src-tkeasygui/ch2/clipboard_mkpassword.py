import secrets
import pyperclip
import TkEasyGUI as sg

# パスワードの候補となる文字列を指定 --- (*1)
upper_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_str = "abcdefghijklmnopqrstuvwxyz"
number_str = "0123456789"
flag_str = "#!@_-"
password_chars = upper_str + lower_str + number_str + flag_str
# 作成する文字数を指定 --- (*2)
password_length = 16
# パスワード文字列を繰り返し生成する --- (*3)
while True:
    p = [secrets.choice(password_chars) for _ in range(password_length)]
    password = "".join(p)
    # パスワードをコピーする --- (*4)
    pyperclip.copy(password)
    # 情報を画面に表示 --- (*5)
    yesno = sg.popup_yes_no(
        "以下のパスワードを作成しクリップボードにコピーしました\n" + \
        f"パスワード: {password}\n気に入りましたか？", 
        title="作成しました")
    if yesno == "Yes":
        break
    print("パスワードを再作成します")
