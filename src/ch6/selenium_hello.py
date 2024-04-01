import time
from selenium import webdriver

# Chromeを起動 --- (*1)
driver = webdriver.Chrome()
# Google検索にアクセス --- (*2)
driver.get('https://www.google.com/search?q=selenium')
# 3秒間待機 --- (*3)
time.sleep(3)
# 終了 --- (*4)
driver.quit()
