def tani_gram(str_x,n,letter_or_word):
    list1 = list()

    if letter_or_word is 'word':
        str_x = str_x.split()

    x = 0   # x：N-gram1文字目のインデックス（初期値0）
    y = n   # y：N-gram末尾の文字のインデックス（初期値n）

    kazoeru = len(str_x)
    kaisu = kazoeru + 1 - n

    for i in range(kaisu):
        list1.append(str_x[x:y])
        x +=  1
        y +=  1
    
    return list1

out = tani_gram('I am an NLPer',2,'word')
print(out)

out = tani_gram('I am an NLPer',2,'letter')
print(out)