import os, time
from selenium import webdriver

# ダウンロードディレクトリを指定 --- (*1)
download_path = os.path.join(os.path.dirname(__file__), "download")
os.makedirs(download_path, exist_ok=True)
# ダウンロードしたいファイルのURLと保存ファイル名(自動決定)を指定 --- (*2)
zip_url = "https://github.com/kujirahand/nadesiko3/archive/refs/tags/3.5.3.zip"
zip_file = os.path.join(download_path, "nadesiko3-3.5.3.zip")

# Chromeの「実験的オプション」を設定 --- (*3)
prefs = {
   "download.default_directory": download_path,
   "savefile.default_directory": download_path
}
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', prefs)

# Chromeを起動してZIPファイルのURLにアクセス --- (*4)
driver = webdriver.Chrome(options=options)
driver.get(zip_url)
# ダウンロード終了まで待機 --- (*5)
while True:
    if os.path.exists(zip_file):
        break
    print("ダウンロード完了を待機します")
    time.sleep(1)
driver.quit()
print("ダウンロード完了:", zip_file)
