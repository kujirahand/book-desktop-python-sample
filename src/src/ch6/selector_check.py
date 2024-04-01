import os
from scraping_test import extract_element

# ローカルファイルを指定 --- (*1)
SCRIPT_DIR = os.path.dirname(__file__)
sample_file = os.path.join(SCRIPT_DIR, "selector_test.html")
sample_url = f"file://{sample_file}"

# <h3>要素を抽出 --- (*2)
print("=== h3 === ")
print(extract_element(sample_url, query="h3"))

# <li>の一覧を抽出 --- (*3)
print("=== li === ")
print(extract_element(sample_url, query="li"))

# 好きな果物を抽出 --- (*4)
print("=== #friuts li === ")
print(extract_element(sample_url, query="#fruits li"))

# class="best"のアイテムを抽出 --- (*5)
print("=== .best === ")
print(extract_element(sample_url, query="li.best"))

