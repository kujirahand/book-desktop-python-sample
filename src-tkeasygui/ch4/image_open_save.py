from PIL import Image
# 画像の読み込み --- (*1)
img = Image.open("image.png")
# 画像のサムネイルを作成 --- (*2)
img.thumbnail((300, 300))
img = img.convert("RGB") # RGB形式に変換
# 色空間をRGBに変換 --- (*3)
img = img.convert("RGB")
# 任意の形式で保存 --- (*4)
img.save("image_thumb.jpg", format="JPEG")
print("保存しました")
