with open('hightemp.txt', encoding = "utf-8") as f: # f：元のファイル
    f_list = f.readlines()                          # f_list：fを１行ずつ区切って展開したデータ（リスト）

col1 = []   # col1：col1.txtに入れるデータを入れるリスト（リスト）
col2 = []   # col2：col2.txtに入れるデータを入れるリスト（リスト）

for f_line in f_list:                       # f_line：f_listの中の１行（文字列）
    f_line_list = f_line.split('\t')        # f_line_list：Tabごとに区切った一行（リスト）
    col1.append(f_line_list[0])             # col1にn行目の１列目を格納
    col2.append(f_line_list[1])             # col2にn行目の２列目を格納

col1_str = '\n'.join(col1)      # col1_str：col1を改行ありの文字列にしたもの（文字列）
col2_str = '\n'.join(col2)      # co21_str：col2を改行ありの文字列にしたもの（文字列）

with open('col1.txt', mode = 'w') as f_col1:
    f_col1.write(col1_str)


with open('col2.txt', mode = 'w') as f_col2:
    f_col2.write(col2_str)