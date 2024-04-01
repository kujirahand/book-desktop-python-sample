import easyocr

# 日本語と英語のテキストを読み取るオブジェクトを作成 --- (*1)
reader = easyocr.Reader(["ja", "en"]) 
# 画像ファイルを指定してテキストを読み取る --- (*2)
result = reader.readtext("shop.png")
# 読み取った内容を表示 --- (*3)
for data in result:
    # 座標, テキスト, 信頼度が取得できる --- (*4)
    _position, text, con = data
    print(f"[{text}](信頼度:{con:.2f})")
