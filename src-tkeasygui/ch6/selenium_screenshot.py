import urllib.parse
import time
from selenium import webdriver

# 検索キーワードを指定 --- (*1)
keyword = "柴犬"
# 検索キーワードをURLエンコード --- (*2)
key_enc = urllib.parse.quote(keyword)
# Chromeを起動 --- (*3)
driver = webdriver.Chrome()
# 柴犬を検索 --- (*4)
driver.get(f"https://www.google.com/search?q={key_enc}")
# 読み込み完了まで最大10秒待つ --- (*5)
driver.implicitly_wait(10)
# スクリーンショットを撮影 --- (*6)
driver.save_screenshot('screenshot.png')
driver.quit() # 終了 
