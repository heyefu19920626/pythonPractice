import re

import requests

from downFiction_diyibanzhu import deleteFile as deleteFile
from downFiction_diyibanzhu import get_html_by_url as getHtmlByUrl


def getAuthor(html):
    regex_author = '<h1>.*?</h1>.*?<p>.*?：(.*?)</p>'
    author = re.findall(regex_author, html, re.S)
    return author[0]

BASE_DIR = 'E:\\fiction\\txt\\'
book_url = "https://yazhouse8.com/E54dc.htm"
prefix = 'https://yazhouse8.com/'

html = getHtmlByUrl(book_url, encode='utf-8')
print('book_url = %s' % book_url)

catalog_file = BASE_DIR + '三兄弟的淫荡乱伦_catalog.txt'
content_file = BASE_DIR + '三兄弟的淫荡乱伦.txt'
deleteFile(catalog_file)
deleteFile(content_file)


regex_catalog = '<a class="img-center" target="_blank" href="(.*?)">(.*?)</a></p>'
catalogs = re.findall(regex_catalog, html)
with open(catalog_file, 'w', encoding='utf-8') as f:
    for catalog in catalogs:
        f.write(catalog[1])
        f.write('\n')
for catalog in catalogs:
    catalog_url = prefix + catalog[0]
    catalog_text = catalog[1]
    print('Start:' + catalog_text)
    response_chaper = requests.get(catalog_url)
    response_chaper.encoding = 'utf-8'
    content = response_chaper.text
    regex_chaper = '<div class="img-center">(.*?)</div>'
    content = re.findall(regex_chaper,content, re.S)
    if len(content) > 0:
        content = content[0].replace('<br />', '')
        content = content.replace('&nbsp;', '')
        content = content.replace('<p>', '\n')
        content = content.replace('第\\d章', '')
        with open(content_file, 'a', encoding='utf-8') as f:
            f.write(catalog_text + '\n')
            f.write(content + '\r\n')
        print('Over:' + catalog_text)
    else:
        print('Error:' + catalog_text)
        print('Error:' + catalog_url)
    # break


print('Over')