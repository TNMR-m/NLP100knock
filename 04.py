str1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str1 = str1.replace(",","")
str1 = str1.replace(".","")
str2 = str1.split()

str3 = {}
a = 0

l = [1,5,6,7,8,9,15,16,19]

for a,i in enumerate(str2,1):
    str5 = i
    # if a == 0 or a == 4 or a == 5 or a == 6 or a == 7 or a == 8 or a == 14 or a == 15 or a == 18:
    if a in l:
        str4 = str5[:1]
    else:
        str4 = str5[:2]
    str3[str4] = a

print(str3)