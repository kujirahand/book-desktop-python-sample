name_list = ["Taro", "Jiro", "Sabu"]

# enumerateを使う場合 --- (*1)
for i, name in enumerate(name_list):
    print(i+1, name)

# rangeを使う場合 --- (*2)
for i in range(len(name_list)):
    name = name_list[i]
    print(i+1, name)
