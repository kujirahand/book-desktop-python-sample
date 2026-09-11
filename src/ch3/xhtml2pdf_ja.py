import xhtml2pdf_patch_for0_2
from xhtml2pdf import pisa

html = """
<html><head>
<title>日本語を表示しよう</title>
<style>
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

with open("xhtml2pdf_ja.pdf", "wb") as pdf_file:
    pisa.CreatePDF(html, dest=pdf_file)
