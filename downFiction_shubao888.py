import requests
import json
import re
from downFiction_diyibanzhu import getHtmlByUrl as getHtmlByUrl
from downFiction_diyibanzhu import getName as getName
from downFiction_diyibanzhu import deleteFile as deleteFile

def getAuthor(html):
    regex_author = '<h1>.*?</h1>.*?<p>.*?：(.*?)</p>'
    author = re.findall(regex_author, html, re.S)
    return author[0]

BASE_DIR = 'E:\\fiction\\txt\\'
book_url = "https://www.shubao888.com/book/1/1937/"
prefix = 'https://www.shubao888.com'

html = getHtmlByUrl(book_url)
print('book_url = %s' % book_url)
name = BASE_DIR + '《' + getName(html) + '》'
author = getAuthor(html)
print(author)

catalog_file = name +  '作者：' + author + '_catalog.txt'
content_file = name +  '作者：' + author + '.txt'
deleteFile(catalog_file)
deleteFile(content_file)


regex_catalog = '<dd><a\s+?href=["|\'](.*?)["|\']>(.*?)</a></dd>'
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
    response_chaper.encoding = 'gbk'
    content = response_chaper.text
    regex_chaper = '<div id="content">(.*?)</div>'
    content = re.findall(regex_chaper,content, re.S)
    if len(content) > 0:
        content = content[0].replace('<br />', '')
        content = content.replace('&nbsp;', '')
        content = content.replace('\r', '')
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