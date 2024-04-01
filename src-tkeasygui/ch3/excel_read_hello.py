import TkEasyGUI as sg
import openpyxl as xl
# Excelファイルを読み込む --- (*1)
workbook = xl.load_workbook("./excel_hello.xlsx")
# アクティブなシートを取得 --- (*2)
sheet = workbook.active
# セルA1の内容を読む --- (*3)
val = sheet["A1"].value
sg.popup(val, title="A1の内容")
# ワークブックを閉じる --- (*4)
workbook.close()
