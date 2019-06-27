import gzip
import json
import re

f1_list = []

with gzip.open('jawiki-country.json.gz', 'r') as f1:
    for f1_line in f1:
        f1_column = json.loads(f1_line)
        f1_list.append(f1_column)

f2_date = ''.join(str(f1_list))

'''
with open('test_json.txt', 'w', encoding = 'utf-8') as f2:
    f2.write(f2_date)
    # 辞書型の活用、と改行の変換？……
'''

# content = r'test_json.txt'
content = f2_date
pattern = 'イギリス'

repatter = re.compile(pattern)
result = repatter.match(content)

print(result)