import requests
import json
import re

book_url = "http://www.123xiaoqiang.me/10/10724/"
prefix = 'http://www.123xiaoqiang.me'

response = requests.get(book_url)
response.encoding = 'gbk'
html = response.text
# with open("banzhu111.html", "w", encoding="utf-8") as f:
#     f.write(html)

regex_catalog = '<li><a href="(.*?)">(【我的母女花】.*?)</a></li>'
catalogs = re.findall(regex_catalog, html)
with open('123xiaoqiang_catalog.txt', 'w', encoding='utf-8') as f:
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
    with open('chaper.html', 'w', encoding='utf-8') as f:
        f.write(content)
    regex_chaper = '<div id=content name="content"><P>(.*?)</P>'
    content = re.findall(regex_chaper,content, re.S)
    if len(content) > 0:
        content = content[0].replace('<br />', '')
        content = content.replace('&nbsp;', '')
        content = content.replace('\r', '')
        content = content.replace('第\\d章', '')
        with open('123xiaoqiang_content.txt', 'a', encoding='utf-8') as f:
            f.write(catalog_text + '\n')
            f.write(content + '\r\n')
        print('Over:' + catalog_text)
    else:
        print('Error:' + catalog_text)
        print('Error:' + catalog_url)
    # break


print('Over')