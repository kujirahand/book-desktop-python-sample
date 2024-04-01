from PIL import Image, ImageFilter, ImageChops, ImageOps, ImageEnhance
# 画像の読み込み --- (*1)
img = Image.open("nami.jpg")
# コントラストを強調 --- (*2)
img = ImageEnhance.Contrast(img).enhance(2.0)
# 線画抽出 --- (*3)
gray1 = img.convert("L") # グレイスケールに変換
gray2 = gray1.filter(ImageFilter.MaxFilter(5)) # 最大フィルタ
line_img = ImageChops.difference(gray1, gray2) # 差異を検出
line_img = ImageOps.invert(line_img) # 反転
# PNG形式で保存 --- (*4)
line_img.save("nami_line.png")
print("保存しました")
