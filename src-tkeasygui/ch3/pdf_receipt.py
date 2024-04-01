import os
import datetime
import math
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import B6, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch, mm, cm

# ひな形ファイルなどの指定 --- (*1)
script_dir = os.path.dirname(__file__)
template_file =  os.path.join(script_dir, "receipt.png")
font_file = os.path.join(script_dir, "ipaexg00401", "ipaexg.ttf")
tax_rate = 0.1 # 税率の指定

# 領収証を作成する関数 --- (*2)
def make_receipt(output_file, name, memo, price):
    # 税込み金額を計算
    tax = math.ceil(price * tax_rate)
    price_n_tax = price + tax
    # 日付を取得
    date_a = datetime.datetime.now().strftime("%Y-%m-%d").split("-")
    # フォントの埋め込み --- (*3)
    pdfmetrics.registerFont(TTFont("IPAexGothic", font_file))
    # 用紙サイズを指定してキャンバスを作成 -- (*4)
    page = canvas.Canvas(output_file, pagesize=landscape(B6))
    # キャンバスに合わせて画像を描画 --- (*5)
    w, h = Image.open(template_file).size # 画像サイズを得る
    r = B6[1] / w
    pdf_h, pdf_w = int(h * r), int(w * r)
    page.drawImage(template_file, 0, 0, width=pdf_w, height=pdf_h)
    # 領収証に書き込みを行う --- (*6)
    page.setFont("IPAexGothic", 20)
    page.drawCentredString(150, 240, name) # 宛名を描画
    page.drawString(120, 185, f"￥{price_n_tax:,}-") # 金額を桁を区切って描画
    page.setFont("IPAexGothic", 12)
    page.drawString(85, 153, f"{memo}") # 但し書きを描画
    page.drawRightString(215, 65, f"￥{price:,}-") # 税抜き金額を桁を区切って描画
    page.drawRightString(215, 39, f"￥{tax:,}-") # 消費税を桁を区切って描画
    page.drawString(55, 55, f"{int(tax_rate*100)}") # 税率を描画
    page.drawString(327, 287, f"{date_a[0]}") # 日付(年)を描画
    page.drawString(380, 287, f"{date_a[1]}") # 日付(月)を描画
    page.drawString(420, 287, f"{date_a[2]}") # 日付(日)を描画
    # ファイルに保存 --- (*7)
    page.save()

if __name__ == "__main__":
    # 書き込む内容を指定 --- (*8)
    output_file = os.path.join(script_dir, "pdf_receipt.pdf")
    make_receipt(
        output_file,
        name="山田 太郎",
        memo="文房具代として",
        price=1000)
