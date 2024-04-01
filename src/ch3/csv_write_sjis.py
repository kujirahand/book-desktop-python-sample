import csv
# UTF-8の「frutis.csv」を読み込む --- (*1)
result = []
with open("fruits.csv", "r", encoding="utf-8") as fp:
    reader = csv.reader(fp)
    for row in reader:
        result.append(row)

# SJISの「fruits_sjis.csv」に出力 --- (*2)
with open("fruits_sjis.csv", "w", encoding="sjis") as fp:
    writer = csv.writer(fp)
    writer.writerows(result)
