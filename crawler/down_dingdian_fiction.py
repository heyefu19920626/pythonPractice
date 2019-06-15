import requests
import json
import re
from down_basic import getHtmlByUrl as getHtmlByUrl
from down_basic import deleteFile as deleteFile
from down_basic import getBaseDir as getBaseDir
from down_basic import parse as parse
from down_basic import isNull as isNull
from down_basic import saveFile as saveFile

BASE_DIR = getBaseDir() + "\\txt\\"

def getAuthor(html):
    regex_author = '<h1>.*?</h1>.*?<p>.*?：(.*?)</p>'
    author = re.findall(regex_author, html, re.S)
    return author[0]

book_url = "https://www.booktxt.net/2_6161/"
prefix = 'https://www.booktxt.net/2_6161/'
html = getHtmlByUrl(book_url)

book_name_regex = '<h1>(.*?)</h1>'
result = parse(html, book_name_regex)
isNull(result)
book_name = result[0]
print(book_name)

book_txt = BASE_DIR + book_name + '.txt'
book_catalog_txt = BASE_DIR + book_name + "_catalog.txt"
deleteFile(book_txt)
deleteFile(book_catalog_txt)

catalog_all_regex = '正文</dt>(.*?)</dl>'
result = parse(html, catalog_all_regex)
isNull(result)
catalogs_regex = '<dd><a href="(.*?)">(.*?)</a></dd>'
result = parse(result[0], catalogs_regex)
isNull(result)
catalogs = result

for catalog in catalogs:
    print(catalog[1] + '...')
    catalog_url = prefix + catalog[0]
    html = getHtmlByUrl(catalog_url)
    content_regex = '<div id="content">(.*?)</div>'
    result = parse(html, content_regex)
    isNull(result)
    content = catalog[1] + '\n\n' + result[0]
    content = content.replace('<br />', '\n')
    content = content.replace('&nbsp;', ' ')
    saveFile(book_txt, content, "a", "utf-8")
    saveFile(book_catalog_txt, catalog[1], "a", "utf-8")

print('Over')