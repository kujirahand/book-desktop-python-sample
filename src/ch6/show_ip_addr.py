import platform, subprocess, re
import pyperclip # クリップボード操作
import PySimpleGUI as sg
# import TkEasyGUI as sg

def get_ip_address():
    # IPアドレスを取得するコマンドを実行 --- (*1)
    cmd = "ipconfig" if platform.system() == "Windows" else "ifconfig"
    result = subprocess.run([cmd], text=True, stdout=subprocess.PIPE)
    # 結果を確認する --- (*2)
    if result.returncode != 0:
        sg.popup("IPアドレスの取得に失敗しました")
        return []
    # 正規表現でIPアドレス(IPv4)を取り出す --- (*3)
    text = result.stdout
    addr = re.findall(r"([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", text)
    # 255で終わる(または始まる)アドレスを除外 --- (*4)
    return filter(lambda n:
            n.split(".")[3] != "255" and n.split(".")[0] != "255", addr)

def show_window(ip_list):
    # IPアドレスの結果を表示 --- (*5)
    window = sg.Window("IPアドレス", layout=[
        [sg.Text("IPアドレス")],
        [sg.Button(ip) for ip in ip_list],
        [sg.Button("閉じる")]])
    while True:
        event, _ = window.read()
        if event in ["閉じる", sg.WIN_CLOSED]:
            break
        # ボタンクリックでクリップボードにコピー --- (*6)
        pyperclip.copy(event)
        sg.popup(f"{event}をコピーしました")

if __name__ == "__main__":
    show_window(get_ip_address())
