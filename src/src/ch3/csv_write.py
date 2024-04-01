import csv
# リスト型のデータ --- (*1)
data = [
    ["ABCD, Inc", 500000, 4],
    ["WXYZ LLC", 800000, 4],
    ["DEFG, Inc", 350000, 3],
    ["4567 Group Corp", 600000, 5],
    ["GHIJ, Inc", 450000, 4],
]
# CSV形式でファイルに書き込む --- (*2)
with open("company2.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
