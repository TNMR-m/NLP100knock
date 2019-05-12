with open('col1.txt') as col1_f:
    col1_str = col1_f.read()    # ファイル全体を文字列として読む

with open('col2.txt') as col2_f:
    col2_str = col2_f.read()    # 同上

col1_list = col1_str.split()    # ファイルを行ごとに区切ってリストにする
col2_list = col2_str.split()    # 同上

merge_list = []

for col1, col2 in zip(col1_list, col2_list):
    merge_str = col1 + '\t' + col2  # １列目と２列目をTab区切りで結合
    merge_list.append(merge_str)    # 結合した文字列をリストに追加
    merge_list.append('\n')         # 行ごとの改行

merge = ''.join(merge_list)         # リストを文字列に変換する

with open('merge.txt', 'w') as merge_f:
    merge_f.write(merge)            # 作成したデータを新しいファイルに書き込み