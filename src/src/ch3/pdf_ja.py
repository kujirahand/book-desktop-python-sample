import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, mm, cm

# フォントの埋め込み --- (*1)
script_dir = os.path.dirname(__file__)
font_path = os.path.join(script_dir, "ipaexg00401", "ipaexg.ttf")
pdfmetrics.registerFont(TTFont("IPAexGothic", font_path))
# 表示したい格言を指定 --- (*2)
text = "黙っているのに時があり，話すのに時がある。"
# A4サイズを準備 -- (*3)
page = canvas.Canvas("pdf_ja.pdf", pagesize=portrait(A4))
cols = 12
margin = 10
tile = (A4[0] - margin*2) / cols
rows = int((A4[1] - margin*2) / tile)
page.setFont("IPAexGothic", tile * 0.5) # フォントを指定 --- (*4)
for y in range(rows):
    for x in range(cols):
        # どの文字を描画するか計算 --- (*5)
        i = (x + y * cols)
        c = text[i % len(text)]
        # 座標を計算 --- (*6)
        xx = (x * tile + margin)
        yy = A4[1] - ((y + 1) * tile + margin)
        # 方眼紙を描画 --- (*7)
        page.rect(xx, yy, tile, tile, stroke=1, fill=0)
        # アルファベットを描画 --- (*8)
        page.drawString(xx + 9, yy + 9, c)
# ファイルに保存 --- (*9)
page.save()
