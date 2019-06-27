from sys import argv

# pythonファイル、テキストファイル、分割数をコマンドライン引数に

f_list = []
f_list2 = []
result = []

# with open(argv[1], encoding = 'utf-8') as f:
with open('hightemp.txt', encoding = 'utf-8') as f:
    for line in f:
        f_list.append(line)

'''
if argv[2] != 0:
    cut_num = len(f_list) / argv[2] # cut_num : 分割したひとつごとの行数
else:
    cut_num = len(f_list)
'''
cut_num = len(f_list) / 3

# for i in range(argv[2]):
for i in range(1, 3):
    for j in range(int(cut_num)):
        f_list2.append(f_list[j+j*i])   # list
    result.append(f_list2)

print(result)