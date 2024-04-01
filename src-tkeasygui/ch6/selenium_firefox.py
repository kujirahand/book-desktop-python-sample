import time
from selenium import webdriver

# Firefoxを起動 --- (*1)
driver = webdriver.Firefox()
# Google検索にアクセス
driver.get('https://www.google.com/search?q=selenium')
driver.implicitly_wait(10)
time.sleep(3)
# スクリーンショットを保存
driver.save_screenshot('screenshot_firefox.png')
driver.quit()
