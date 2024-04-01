# (1) CSVデータをテキストとして読み込みカンマで区切る - 不完全で注意が必要
result = []
with open("fruits.csv", "r", encoding="utf-8") as fp:
    # 1行ずつ読み込む
    for line in fp.readlines():
        row = line.split(",") # カンマでデータを区切るだけ
        result.append(row)
# 正しく読めたか確認する
orange = result[2]
print(f"(1) 果物:{orange[0]} 産地:{orange[1]}")

# (2) CSVモジュールを使って読み込む
import csv
result = []
with open("fruits.csv", "r", encoding="utf-8") as fp:
    csv_reader = csv.reader(fp)
    for row in csv_reader:
        result.append(row)
# 正しく読めたか確認する
orange = result[2]
print(f"(2) 果物:{orange[0]} 産地:{orange[1]}")
