from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import inch, mm, cm

# A4サイズを準備 -- (*1)
page = canvas.Canvas('pdf_line_text.pdf', pagesize=portrait(A4))

# 方眼紙とテキストを描画 --- (*2)
cols = 26
margin = 10
tile = (A4[0] - margin*2) / cols
rows = int((A4[1] - margin*2) / tile)
page.setFontSize(tile * 0.5) # フォントサイズを指定 --- (*3)
for y in range(rows):
    for x in range(cols):
        i = (x + y) % 26
        # 座標を計算 --- (*4)
        xx, yy = (x * tile + margin, y * tile + margin)
        # 方眼紙を描画 --- (*5)
        page.rect(xx, yy, tile, tile, stroke=1, fill=0)
        # アルファベットを描画 --- (*6)
        page.drawString(xx + 8, yy + 7, chr(ord('A') + i))

# ファイルに保存 --- (*7)
page.save()
