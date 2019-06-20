str1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

str2 = str1.replace(",","")
str2 = str2.replace(".","")

list1 = str2.split()
dict1 = {}

l = [1, 5, 6, 7, 8, 9, 15, 16, 19]  # 一文字だけ取るものをリストアップ

for i, s in enumerate(list1, 1):    # 初期値1
    if i in l:
        dict1[i] = s[:1]
    else:
        dict1[i] = s[:2]

print(dict1)