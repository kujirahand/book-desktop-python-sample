from xhtml2pdf import pisa
# PDFを生成するHTML --- (*1)
html = """
<html><head>
<title>日本語を表示しよう</title>
<style>
    /* 日本語フォントの定義 --- (*2) */
    @font-face {
        font-family: "ipaexg";
        src: url("./ipaexg00401/ipaexg.ttf");
    }
    body { font-family: "ipaexg"; }
</style>
<body>
    <h1 style="font-size: 8em">
    Hello!<br>
    こんにちは!<br>
    </h1>
</body></html>
"""
# ファイルを開いてPDFを生成 --- (*3)
with open('xhtml2pdf_ja.pdf', 'wb') as pdf_file:
    pisa.CreatePDF(html, dest=pdf_file)
