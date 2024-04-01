import TkEasyGUI as sg

# 電卓のボタンを定義する --- (*1)
calc_buttons = [
    ["C", "←", "//", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "%", "="]
]
# 電卓で利用するフォントを定義する --- (*2)
font = ("Helvetica", 20)
# 基本的なレイアウトを作成 --- (*3a)
layout = [
    # 電卓上部のテキストを作成
    [sg.Text("0",
             key="-output-", 
             background_color="white", text_color="black",
             font=font,
             expand_x=True)],
]
# 上記定義に応じてレイアウトを作成する --- (*4)
for row in calc_buttons:
    buttons = []
    for ch in row:
        # ボタンを作成する --- (*5)
        btn = sg.Button(
            ch, # ボタンのラベル
            key=f"-btn{ch}", # キーを指定
            size=(3, 1), # ボタンのサイズ
            font=font, # フォントを指定
        )
        buttons.append(btn)
    layout.append(buttons)
# ウィンドウを作成する --- (*6)
window = sg.Window("電卓", layout)
# イベントループ
output = "0"
while True:
    # イベントを取得する
    event, _ = window.read()
    # 閉じるボタンの時
    if event == sg.WINDOW_CLOSED:
        break
    # 何かしらのボタンが押された時 --- (*7)
    if event.startswith("-btn"):
        # ラベルとテキストの値を取得する --- (*8)
        ch = window[event].GetText()
        # テキストが空(0かエラー)ならクリアする --- (*9)
        if output == "0" or output.startswith("E:"):
            output = ""
        # ラベルに応じて処理を変更 --- (*10)
        if ch == "C": # クリアキー
            output = "0"
        elif ch == "←": # バックスペースキー
            output = output[:-1]
        elif ch == "=": # 計算ボタンー --- (*11)
            try:
                output = str(eval(output))
            except Exception as e:
                output = "E:" + str(e)
        else:
            # それ以外のキーはそのまま追加する --- (*12)
            output += ch
        # 画面上部のディスプレイを更新 --- (*13)
        window["-output-"].update(output)
window.close()
