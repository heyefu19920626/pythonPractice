from crawler.down_basic import getBaseDir as getBaseDir
from crawler.down_basic import getHtmlByUrl as getHtmlByUrl
from crawler.down_basic import parse as parse
from crawler.down_basic import isNull as isNull
from crawler.down_basic import deleteFile as deleteFile
from crawler.down_basic import saveFile as saveFile

def format_content(content):
    content = content.replace('&nbsp;', '')
    content = content.replace('<br />', '')
    return content

book_url = "http://www.diyibanzhu.info/9/9901/"
prefix = 'http://www.diyibanzhu.info/9/9901/'

BASE_DIR = getBaseDir()

html = getHtmlByUrl(book_url)

# 获取书名
title_regex = '<h1>(.*?)</h1>'
title_result = parse(html, title_regex)
isNull(title_result)
title = title_result[0]

# 获取作者
# author_regex = '<span>作者：(.*?)</span>'
# author_result = parse(html, author_regex)
# isNull(author_result)
# author = '作者：' + author_result[0]
author = '作者：未知'

# 获取目录
catalog_div_regex = '<div class="ml_list">(.*?)</div>'
catalog_div_result = parse(html, catalog_div_regex)
isNull(catalog_div_result)
html = catalog_div_result[0]
catalog_regex = '<li><a href="(.*?)">(.*?)</a></li>'
catalog_result = parse(html, catalog_regex)
isNull(catalog_result)

# 删除旧文件
text_file = BASE_DIR + '《' + title + '》' + author + '.txt'
catalog_file = BASE_DIR + '《' + title + '》' + author + '_catalog.txt'
deleteFile(text_file)
deleteFile(catalog_file)

# catalog_result = catalog_result[(len(catalog_result)-1) : ]

# 获取正文
for catalog in catalog_result:
    print('正在抓取:' + catalog[1])
    catalog_url = prefix + catalog[0]
    html = getHtmlByUrl(catalog_url)
    content_regex = '<p class="articlecontent" id="articlecontent">(.*?)</p>'
    content_result = parse(html, content_regex)
    isNull(content_result)
    content = catalog[1] + '\n\n' + format_content(content_result[0])
    saveFile(text_file, content, 'a')
    saveFile(catalog_file, catalog[1], 'a')

print('Over')
