# リストの内包表記を使って100個の要素を作る
msg_list = [ f"大好き{i}。" for i in range(1, 100+1) ]
# リストを結合して表示
print( "".join(msg_list) )
