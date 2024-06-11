# キーを指定しない場合の例
import PySimpleGUI as sg
# import TkEasyGUI as sg

# ウィンドウの作成 (keyを指定しなかった場合) --- (*1)
window = sg.Window("インチからセンチへ", layout=[
    [sg.Text("インチを入力してください")],
    [sg.Input("1"), sg.Button("変換")],
])
while True:
    event, values = window.read()
    print(event, values) # コンソールに値を出力
    if event == sg.WIN_CLOSED:
        break
    if event == "変換": # 変換ボタンを押した時
        try:
            # 最初の sg.Input の値を key=0 で取得できる --- (*2)
            inch = float(values[0])
            cm = inch * 2.54 # センチに変換
            sg.popup(f"{inch}インチは、{cm}センチ")
        except:
            sg.popup("数値を入力してください。")
window.close()

