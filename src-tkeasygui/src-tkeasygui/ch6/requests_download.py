import os, requests

# ダウンロードディレクトリを指定
download_path = os.path.join(os.path.dirname(__file__), "download")
os.makedirs(download_path, exist_ok=True)
# ダウンロードURLと保存ファイル名を指定
zip_url = "https://github.com/kujirahand/nadesiko3/archive/refs/tags/3.5.3.zip"
zip_file = os.path.join(download_path, "nadesiko3-3.5.3.zip")

# ファイルをダウンロードして保存
with open(zip_file, "wb") as f:
    res = requests.get(zip_url)
    f.write(res.content)
