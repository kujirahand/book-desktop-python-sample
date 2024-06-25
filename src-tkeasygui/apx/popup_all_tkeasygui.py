import TkEasyGUI as eg

# 色選択ダイアログをポップアップ --- (*20)
print(eg.popup_color("[20] popup_color"))
# 任意のボタンをポップアップ --- (*21)
print(eg.popup_buttons("[21] popup_buttons",
    buttons=["リンゴ", "バナナ", "ミカン"]))
# リストボックスをポップアップ --- (*22)
print(eg.popup_listbox(title="[22] popup_list",
    message="好きな果物を選んでください",
    items=["リンゴ", "バナナ", "ミカン"]))
