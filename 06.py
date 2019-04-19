def tani_gram_l(str_x,n):
    list1 = list()

    x = 0   # x：N-gram1文字目のインデックス（初期値0）
    y = n   # y：N-gram末尾の文字のインデックス（初期値n）

    mojisu = len(str_x)
    kaisu = mojisu + 1 - n

    for i in range(kaisu):
        list1.append(str_x[x:y])
        x +=  1
        y +=  1
    
    return list1

str1 = tani_gram_l('paraparaparadise',2)
str2 = tani_gram_l('paragraph',2)

x = set(str1)
y = set(str2)

print('X：',x,'Y：',y)

wa = x | y
print('和集合：',wa)

seki = x & y
print('積集合：',seki)

sa = x - y
print('差集合：',sa)

if 'se' in wa:
    print('"se"はXとYの和集合に含まれます')
else:
    print('"se"はXとYの和集合に含まれません')