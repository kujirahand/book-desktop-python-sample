import PySimpleGUI as sg

# 質問する果物 --- (*1)
fruits = ["リンゴ", "ミカン", "イチゴ", "バナナ", "ブドウ"]
# 繰り返し質問を行う --- (*2)
points = 0
for name in fruits:
    r = sg.popup_yes_no(f"{name}は好きですか?", title="質問")
    # Yesが押されたらpointsを1加算する --- (*3)
    if r == "Yes":
        points += 1
# 結果を表示 --- (*4)
sg.popup(f"好きな果物の点数は、{points}点でした。", title="結果")
