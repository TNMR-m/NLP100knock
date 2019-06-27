from sys import argv

# pythonファイル、テキストファイル、分割数をコマンドライン引数に

f_list = []
f_list2 = []

# 「ファイルをN分割」
# https://www.python.ambitious-engineer.com/archives/1843


with open(argv[1], encoding = 'utf-8') as f:
    for line in f:
        f_list.append(line)
        
gyousu = len(f_list) / argv[2]
# 全行数÷分割数の商の数だけ前からとる

# 前から分割数分取る→変数に分割数足す→続きから(変数)行まで取る→変数が全体の行数を超えたらその一周を終えてループ終了

for i in range(argv[2] + ):
    f_list2.append(f_list[i])