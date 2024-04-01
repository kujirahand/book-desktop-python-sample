from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait

# 作成するファイル名を指定
pdf_file = "hello.pdf"

# A4サイズのPDFを作成 --- (*1)
page = canvas.Canvas(pdf_file, pagesize=portrait(A4))
# ページに文字を描画 --- (*2)
page.setFontSize(80)
page.drawString(20, 700, "Hello!")
# PDFを保存 -- (*3)
page.save()
