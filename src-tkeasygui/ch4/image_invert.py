from PIL import Image, ImageOps
# 画像の読み込み --- (*1)
img = Image.open("nami.jpg")
# ネガポジ変換 --- (*2)
img = ImageOps.invert(img)
# 任意の形式で保存 --- (*3)
img.save("nami_invert.jpg")
print("保存しました")
