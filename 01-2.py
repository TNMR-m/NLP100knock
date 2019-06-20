from math import ceil   # mathライブラリからceil(切り上げ)をインポート

str1 = 'パタトクカシー'
list1 = []

for i in range(ceil(len(str1) / 2)): # 文字数/2 回ループ（余り切り上げ）
    list1 += str1[i * 2]

result = ''.join(list1) # リストを文字列に戻してresultとする

print(result)