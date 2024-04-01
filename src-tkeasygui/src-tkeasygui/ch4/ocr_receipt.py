import re
from PIL import Image
import easyocr

# 対象画像ファイル --- (*1)
image_path = "receipt.png"
# 画像サイズからだいたいの位置を考慮 --- (*2)
(w, h) = Image.open(image_path).size
x_range = (1/3 * w, 2/3 * w)
y_range = (0/3 * h, 1/3 * h)
print("画像サイズ:", (w, h))
print("検索範囲:", x_range, y_range)

# EasyOCRのオブジェクトを作成して読み取る --- (*3)
reader = easyocr.Reader(["ja", "en"])
result = reader.readtext(image_path)
# 読み取った内容から金額を検索 --- (*4)
for data in result:
    # 座標, テキスト, 信頼度が取得できる --- (*5)
    pos, text, con = data
    # pos[0](左上)とpos[1](右下)の中央を計算 --- (*6)
    cx = (pos[0][0] + pos[2][0]) / 2
    cy = (pos[0][1] + pos[2][1]) / 2
    # 検索範囲にあるテキストだけを表示 --- (*7)
    if x_range[0] < cx < x_range[1] and \
       y_range[0] < cy < y_range[1]:
        # 数字があることを確認 --- (*8)
        if re.search(r"[0-9]", text):
            print(f"金額: {text} (信頼度:{con:.2f})")
