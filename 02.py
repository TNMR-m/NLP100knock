str1 = 'パトカー'
str2 = 'タクシー'
list1 = []

for i in range(len(str1)):          # 文字数分ループする
    list1 += str1[i] + str2[i]

result = ''.join(list1)
print(result)