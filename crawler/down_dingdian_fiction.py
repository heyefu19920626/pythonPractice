import requests
import json
import re
import time
from down_basic import getHtmlByUrl as getHtmlByUrl
from down_basic import deleteFile as deleteFile
from down_basic import getBaseDir as getBaseDir
from down_basic import parse as parse
from down_basic import isNull as isNull
from down_basic import saveFile as saveFile

STATUS = 1

BASE_DIR = getBaseDir() + "\\txt\\"

def getAuthor(html):
    regex_author = '<h1>.*?</h1>.*?<p>.*?：(.*?)</p>'
    author = re.findall(regex_author, html, re.S)
    return author[0]

book_url = "https://www.booktxt.net/8_8112/"
prefix = 'https://www.booktxt.net/8_8112/'
html = getHtmlByUrl(book_url)

book_name_regex = '<h1>(.*?)</h1>'
result = parse(html, book_name_regex)
isNull(result)
book_name = result[0]
print(book_name)

book_txt = BASE_DIR + book_name + '.txt'
book_catalog_txt = BASE_DIR + book_name + "_catalog.txt"
# 是否从头开始
if STATUS == 0:
    deleteFile(book_txt)
    deleteFile(book_catalog_txt)

catalog_all_regex = '正文</dt>(.*?)</dl>'
result = parse(html, catalog_all_regex)
isNull(result)
catalogs_regex = '<dd><a href="(.*?)">(.*?)</a></dd>'
result = parse(result[0], catalogs_regex)
isNull(result)
catalogs = result

catalogs = catalogs[245:]

tmp = 245
for catalog in catalogs:
    time.sleep(1.5)
    print(str(tmp) + ' ' + catalog[1] + '...')
    catalog_url = prefix + catalog[0]
    for i in range(1,4):
        try:
            html = getHtmlByUrl(catalog_url)
            break
        except Exception as e:
            print('连接错误，重新尝试...')
    content_regex = '<div id="content">(.*?)</div>'
    result = parse(html, content_regex)
    isNull(result)
    content = catalog[1] + '\n\n' + result[0]
    content = content.replace('<br />', '\n')
    content = content.replace('&nbsp;', ' ')
    saveFile(book_txt, content, "a", "utf-8")
    saveFile(book_catalog_txt, catalog[1], "a", "utf-8")
    tmp += 1

print('Over')