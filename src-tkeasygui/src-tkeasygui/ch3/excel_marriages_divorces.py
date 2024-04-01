import TkEasyGUI as sg
import openpyxl as xl

# Excelファイルから婚姻率と離婚率を得る
def read_excelfile():
    # Excelファイルを読み込む --- (*1)
    EXCEL_FILE = "./population_jp.xlsx"
    workbook = xl.load_workbook(EXCEL_FILE)
    # ブックの中のシート「A」を取得 --- (*2)
    sheet = workbook["A"]
    # シート上の任意の情報を得るために列の情報を辞書型で指定 --- (*3)
    columns_info = {
        "都道府県": "I", # "情報" : "列名" の形式で指定
        "婚姻率": "CJ", 
        "離婚率": "CL"}
    result = []
    # 連続でセルの値を取得する(14行から60行まで) --- (*4)
    for row_no in range(14, 60+1):
        line = []
        for _, col_name in columns_info.items():
            # セル名から列番号を得る --- (*5)
            col_no = xl.utils.column_index_from_string(col_name)
            # セルの値を得る --- (*5a)
            val = sheet.cell(row_no, col_no).value
            line.append(val)
        result.append(line)
    workbook.close()
    # 婚姻率と離婚率でソートする --- (*6)
    mar_list = list(sorted(result, key=lambda x: x[1], reverse=True))
    div_list = list(sorted(result, key=lambda x: x[2], reverse=True))
    # ソートした結果から上位10件を取り出す --- (*7)
    top10 = [
        [
            f"{(i+1):02}", # 順位
            f"{mar_list[i][0]} ({mar_list[i][1]})", # 婚姻率
            f"{div_list[i][0]} ({div_list[i][2]})" # 離婚率
        ] for i in range(10)]
    return top10

# テーブルに結果を表示する関数 --- (*8)
def show_table(data):
    layout = [
        [sg.Table(values=data,
            headings=["順位", "婚姻率", "離婚率"],
            auto_size_columns=True,
            expand_x=True, expand_y=True,
            justification="center",
            font=("Arial", 16))],
        [sg.Button("閉じる")]]
    # ウィンドウを作成
    window = sg.Window("都道府県別 婚姻率と離婚率 Top10", layout, size=(400, 300))
    while True: # イベントループ
        event, _ = window.read()
        if event in ["閉じる", sg.WIN_CLOSED]:
            break
    window.close()

if __name__ == "__main__":
    # メイン処理
    data = read_excelfile() # Excelファイルを読み込む
    show_table(data) # テーブルに表示する
