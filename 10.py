from sys import argv

with open(argv[1], encoding="utf-8") as f:
    f_list = f.readlines()

print(len(f_list))