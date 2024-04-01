import pyperclip
import PySimpleGUI as sg
# import TkEasyGUI as sg

# 文字列をコピーする --- (*1)
pyperclip.copy("言葉は刃物なんだ。使い方を間違えると、やっかいな凶器になる。")

# コピーした文字列を取得して画面に表示する --- (*2)
text = pyperclip.paste()
sg.popup(text, title="クリップボードから取得しました")
