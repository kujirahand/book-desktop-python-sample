import html
import re
from xhtml2pdf import pisa

# テキストファイルを読み込む --- (*1)
with open("kokoro.txt", "r", encoding="sjis") as f:
    text = f.read()
    text = text[0:30000] # 冒頭3万字だけを利用
    text = re.sub(r"\《.+?\》", "", text) # ルビを削除
    text = re.sub(r"\［\＃.+?\］", "", text) # 注釈を削除
    text = re.sub(r"([。、])", r"\1 ", text) # 明示的な空白を入れる
    text = html.escape(text, quote=True) # HTML変換
    text = "".join([f'<p>{s}</p>\n' for s in text.split("\n")])

# PDFを生成するHTML --- (*2)
html = f"""
<html><head><meta charset="UTF-8">
<title>複数ページにヘッダを配置</title>
<style>
    /* 日本語フォントの定義 --- (*3) */
    @font-face {{
        font-family: "ipaexg";
        src: url("./ipaexg00401/ipaexg.ttf");
    }}
    body {{
        font-family: "ipaexg"; 
        font-size: 12pt;
    }}
    /* 用紙サイズやヘッダを指定 --- (*4) */
    @page {{
        size: a4 portrait;
        margin: 50pt 10pt 10pt 10pt;
        @frame header_frame {{
            -pdf-frame-content: page-header;
            -pdf-frame-border: 1; /*ヘッダに枠をつける*/
            left: 350pt; width: 230pt; top: 20pt; height: 20pt;
        }}
    }}
</style>
<body>
    <div id="page-header">
        夏目漱石「こころ」(page.<pdf:pagenumber>/<pdf:pagecount>)
    </div>
    <div id="body_content">{text}</div>
</body></html>
"""
# ファイルを開いてPDFを生成 --- (*5)
with open('xhtml2pdf_kokoro.pdf', 'wb') as pdf_file:
    pisa.CreatePDF(html, dest=pdf_file)
