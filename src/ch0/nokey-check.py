# キーを指定しない場合の例
import PySimpleGUI as sg
# import TkEasyGUI as sg

# ウィンドウの作成 (keyを指定しなかった場合) --- (*1)
window = sg.Window("テスト", layout=[
    [sg.Text("ダミー0")],
    [sg.Input("0-input")],
    [sg.Text("ダミー1")],
    [sg.Input("1-input")],
    [sg.Text("ダミー2")],
    [sg.Input("2-input")],
    [sg.Text("ダミー3")],
    [sg.Listbox(["3-listbox"], default_values=["3-listbox"])],
    [sg.Text("ダミー4")],
    [sg.Input("4-input")],
    [sg.Button("値チェック")],
])
while True:
    event, values = window.read()
    print(event, values) # コンソールに値を出力
    if event == sg.WIN_CLOSED:
        break
window.close()

