import TkEasyGUI as sg
import TkEasyGUI as eg

# メッセージを表示する
sg.popup("鉄が鉄を研ぐように人は友を研ぐ。", title="popup")
eg.popup("鉄が鉄を研ぐように人は友を研ぐ。", title="popup")

# エラーがあったことを表示する
sg.popup_error("愚かな人は感情をぶちまける", title="popup_error")
eg.popup_error("愚かな人は感情をぶちまける", title="popup_error")

# 長文を表示する
sg.popup_scrolled("鉄が鉄を研ぐように人は友を研ぐ。" * 10, title="popup_scrolled")
#eg.popup_scrolled("鉄が鉄を研ぐように人は友を研ぐ。" * 10, title="popup_scrolled")
