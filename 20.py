from gzip import open as g_open
import json

def art_uk(file_name):
    with g_open(file_name, 'rt', encoding = 'utf-8') as f0:
        for f0_line in f0:
            f0_dict = json.loads(f0_line)
            if f0_dict['title'] == 'イギリス':
                article_uk = f0_dict['text']
    
    return article_uk
            
print(art_uk('jawiki-country.json.gz'))