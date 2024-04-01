from PIL import Image, ImageFilter
# 画像の読み込み --- (*1)
img = Image.open("nami.jpg")
# ぼかし処理 --- (*2)
img = img.filter(ImageFilter.GaussianBlur(radius=3))
# 任意の形式で保存 --- (*3)
img.save("nami_blur.jpg")
print("保存しました")
