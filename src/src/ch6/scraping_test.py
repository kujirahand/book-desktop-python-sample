import PySimpleGUI as sg
# import TkEasyGUI as sg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# ページ内の要素を抽出して表示する関数 --- (*1)
def extract_element(url, query):
    # Chromeを起動してページにアクセスする --- (*2)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(20) # タイムアウトの時間を設定
    result = ""
    # 要素を抽出 --- (*3)
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, query)
        # 見つかった要素を列挙 --- (*3a)
        for no, ele in enumerate(elements):
            result += f"{no+1:02}: {ele.text}\n"
        return result
    except NoSuchElementException:
        return "見つかりませんでした。"
    finally:
        import time; time.sleep(30)
        driver.quit()

if __name__ == "__main__":
    # ページ内のリンクを抽出して表示 --- (*4)
    result = extract_element(
        "https://uta.pw/sakusibbs/users.php?user_id=1",
        query="#mmlist a")
    # 結果を表示
    result = "[作品の一覧]\n" + result
    sg.popup_scrolled(result, title="結果", size=(40, 20))
