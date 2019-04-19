def cipher(str_x):
    
    str_x = list(str_x)   # 一文字ずつに区切る

    for i in range(len(str_x)):             # 文字のある分繰り返す
        
        if 96 < ord(str_x[i]) < 123:        # 英小文字の場合のみ
            code1 = 219 - ord(str_x[i])     # 219からその文字の文字コードを引く
            code2 = chr(code1)              # 文字コードを文字にする
            str_x[i] = code2                # リストのi文字目（i個目）を置き換える
    
    str_x = ''.join(str_x)                  # 文字列に戻す

    return str_x

a = cipher('AngoUka')
print(a)

a = cipher(cipher('AngoUka'))
print(a)