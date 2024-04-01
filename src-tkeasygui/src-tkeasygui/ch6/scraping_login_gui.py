import os, json
from cryptography.fernet import Fernet
import TkEasyGUI as sg
import scraping_login as login

# ログイン情報の保存したファイルと暗号化用キーファイル --- (*1)
LOGIN_DATA_FILE = "login_data.json.enc"
LOGIN_KEY_FILE = "login_data.key"

# ウィンドウを表示する関数 --- (*2)
def show_window():
    user, pw = load_data()
    # ウィンドウを作成 --- (*3)
    layout = [
        [sg.Text("作詞掲示板のアカウント情報を入力してください。")],
        [sg.Text("ユーザーID:"),
         sg.Input(user, key="user")],
        [sg.Text("パスワード:"),
         sg.Input(pw, key="pass", password_char="*")],
        [sg.Button("CSV取得"), sg.Button("終了")]
    ]
    window = sg.Window("作詞掲示板ログインしてCSVダウンロード", layout)
    # イベントループ
    while True:
        event, values = window.read()
        if event in ["終了", sg.WIN_CLOSED]:
            break
        # 「CSV取得」ボタンを押した時の処理 --- (*4)
        if event == "CSV取得":
            user_id = values["user"]
            password = values["pass"]
            save_data(values)
            # ログイン処理を行う --- (*5)
            if login.main(user_id, password):
                sg.popup("CSVを取得しました")
            else:
                sg.popup("CSVの取得に失敗しました")

# データファイルに保存する関数 --- (*6)
def save_data(data):
    # データをJSON形式に変換 --- (*6a)
    json_str = json.dumps(data)
    # 暗号化のためのキーを作成 --- (*6b)
    key = Fernet.generate_key()
    with open(LOGIN_KEY_FILE, "wb") as fp:
        fp.write(key)
    # 暗号化する --- (*6c)
    fer = Fernet(key)
    bin = fer.encrypt(json_str.encode("utf-8"))
    # ファイルにバイナリモードで書き込む
    with open(LOGIN_DATA_FILE, "wb") as fp:
        fp.write(bin)

# データファイルを読み込む関数 --- (*7)
def load_data():
    if not os.path.exists(LOGIN_DATA_FILE):
        return "", ""
    # 暗号化を解除するためのキーファイルを読む
    with open(LOGIN_KEY_FILE, "rb") as fp:
        key = fp.read()
    # ファイルをバイナリモードで読み込む
    with open(LOGIN_DATA_FILE, "rb") as fp:
        bin = fp.read()
    try:
        # 暗号を解除する --- (*7a)
        fer = Fernet(key)
        json_str = fer.decrypt(bin).decode("utf-8")
        # JSON形式を読み取る --- (*7b)
        data = json.loads(json_str)
    except Exception as e:
        print("ファイルの読み込みに失敗しました", e)
        return "", ""
    return data["user"], data["pass"]

if __name__ == "__main__":
    show_window()
