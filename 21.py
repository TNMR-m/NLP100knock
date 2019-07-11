from gzip import open as g_open
import json
import re

def art_uk(file_name):
    with g_open(file_name, 'rt', encoding = 'utf-8') as f0:
        for f0_line in f0:
            f0_dict = json.loads(f0_line)
            if f0_dict['title'] == 'イギリス':
                article_uk = f0_dict['text']
    
    return article_uk

content = art_uk('jawiki-country.json.gz')
pattern = r'\[\[Category:.*?\]\]'

repatter = re.compile(pattern)
result = repatter.findall(content)

for r_line in result:
    print(r_line)