str1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

str2 = str1.replace(".", "")
str2 = str2.replace(",", "")

list1 = str2.split()
result = []

for s in list1:
    result += str(len(s))

print(result)