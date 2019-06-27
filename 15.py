from sys import argv

f_list = []
f_list2 = []

with open(argv[1], encoding = 'utf-8') as f:
       f_list = f.readlines()
        
f_list.reverse()

for i in range(argv[2]):
       f_list2.append(f_list[i])

f_list2.reverse()

print(f_list2)