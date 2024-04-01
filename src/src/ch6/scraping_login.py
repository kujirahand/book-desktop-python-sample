import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# ユーザーIDとパスワードを指定 --- (*1)
USER_ID = "desktop_book"
PASSWORD = "w7zZh79vqnoLa9ID"

# プログラムのメイン処理
def main(user_id, password):
    # Chromeを起動 --- (*2)
    driver = webdriver.Chrome()
    # ログイン処理を行う --- (*3)
    result = login(driver, user_id, password)
    if not result:
        print("ログイン失敗")
        return False
    # マイページのリンクをクリック --- (*4)
    result = click_link(driver, "★マイページ")
    if not result:
        print("マイページのリンクが見つかりません")
        return False
    # CSVダウンロードのリンクをクリック --- (*5)
    result = click_link(driver, "一覧をCSVでダウンロード")
    if not result:
        print("CSVのダウンロードリンクが見つかりません")
        return False
    time.sleep(10)
    driver.quit()
    return True

# ログインを行う関数 --- (*6)
def login(driver, user_id, password):
    # ログインページにアクセス --- (*7)
    driver.get("https://uta.pw/sakusibbs/users.php?action=login")
    # ユーザーIDとパスワードを入力 --- (*8)
    try:
        driver.find_element(By.ID, "user").send_keys(user_id)
        driver.find_element(By.ID, "pass").send_keys(password)
    except NoSuchElementException as e:
        # IDとパスワードの入力フィールドが見つからない場合は失敗
        print("入力フィールドが見つかりません", e)
        return False
    debug_sleep()
    # ログインボタンをクリック --- (*9)
    try:
        btn = driver.find_element(By.CSS_SELECTOR,
            "#loginForm input[type=submit]")
        btn.click()
        driver.implicitly_wait(20)
    except NoSuchElementException as e:
        # ログインボタンが見つからない場合は失敗
        print("submitボタンが見つかりません", e)
        return False
    # ログインが成功したかどうかを判定 --- (*10)
    try:
        # 「ログアウト」というリンクがあれば成功
        a = driver.find_element(By.LINK_TEXT, "ログアウト")
        print(f"ログインしました(リンク[{a.text}]があります)")
        debug_sleep()
        return True
    except NoSuchElementException as e:
        # 見つからなければ失敗
        print("ログアウトがありません", e)
        return False

# ラベルを指定してリンクをクリックする関数 --- (*11)
def click_link(driver, text):
    try:
        # リンクを探してクリック --- (*12)
        link = driver.find_element(By.LINK_TEXT, text)
        link.click()
        print(f"{text}をクリックしました")
        debug_sleep()
        return True
    except NoSuchElementException as e:
        print(f"{text}が見つかりません", e)
        return False

def debug_sleep(): # デバッグ用に3秒待つ
    time.sleep(3)

if __name__ == "__main__":
    main(USER_ID, PASSWORD)

