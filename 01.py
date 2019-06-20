str1 = 'パタトクカシー'
list1 = []

for i in range(len(str1)):　# 文字数分ループ
    if i % 2 == 0:
        list1 += str1[i]    # 偶数文字目だけ結果文字列に加える
    else:
        continue            # 奇数文字目はスルー

result = ''.join(list1)     # リストを文字列に戻してresultとする

print(result)