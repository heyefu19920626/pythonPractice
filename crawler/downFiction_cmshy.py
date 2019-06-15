import requests
import json
import re

book_url = "http://www.cmshy.net/html/112/index.html"

response = requests.get(book_url)
response.encoding = 'gbk'
html = response.text
with open("1.html", "w", encoding="utf-8") as f:
    f.write(html)

regex_catalog = '<li><p>\\s*<a href="(.*?)">(.*?)</a>\\s*</p></li>'
catalogs = re.findall(regex_catalog, html)
with open('1.txt', 'w', encoding='utf-8') as f:
    for catalog in catalogs:
        f.write(catalog[1])
        f.write('\n')
for catalog in catalogs:
    catalog_url = catalog[0]
    catalog_text = catalog[1]
    print('Start:' + catalog_text)
    response_chaper = requests.get(catalog_url)
    response_chaper.encoding = 'gbk'
    content = response_chaper.text
    with open('chaper.html', 'w', encoding='utf-8') as f:
        f.write(content)
    regex_chaper = '<div class="content" id="content" style="font-size: 14px;">(.*?)</div>'
    content = re.findall(regex_chaper,content, re.S)
    if len(content) > 0:
        content = content[0].replace('<br />', '')
        content = content.replace('&nbsp;', '')
        content = content.replace('\r', '')
        content = content.replace('第\\d章', '')
        with open('2.txt', 'a', encoding='utf-8') as f:
            f.write(catalog_text + '\n')
            f.write(content + '\r\n')
        print('Over:' + catalog_text)
    else:
        print('Error:' + catalog_text)
        print('Error:' + catalog_url)
    # with open('test.txt', 'w', encoding='utf-8') as f:
        # f.write(content)


    # break
print('Over')