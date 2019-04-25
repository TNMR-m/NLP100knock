def kansu09(str_x):
    str_x = str_x.split()   # 文を単語ごとに分解する

    a = 0

    from random import shuffle                         # シャッフルをインポート

    for i in str_x:
        str1 = str_x[a]                   # 現在扱っている単語をstr1とする
        mojisu = len(str_x[a])            # 現在扱っている単語の文字数   
        
        if mojisu > 4:                    # ！　単語の文字数が4文字より多い時、最初と最後以外の文字をシャッフル
            nakami1 = str1[1:-1]          # 単語の2～最後から一つ手前の文字までを取り出す
            nakami2 = list(nakami1)       # ↑ を一文字ずつに区切ってリストにする
            shuffle(nakami2)       # 中身をシャッフル
            nakami1 = ''.join(nakami2)    # 中身を文字列に戻す
            b = str1[:1] + nakami1 + str1[-1:]  # 最初＆最後の文字とくっつける
            str_x[a] = b                  # 元のリストの単語を生成した文字列で置き換える

        a += 1                            # ループを一つ進める
        
    str_y = ' '.join(str_x)     # リストを文字列に戻す

    return str_y

str2 = kansu09("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
print(str2)