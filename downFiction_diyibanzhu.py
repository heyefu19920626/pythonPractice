import requests
import json
import re



def getHtmlByUrl(url, encode='gbk'):
    """根据url获取html内容"""
    response = requests.get(url)
    response.encoding = encode
    html = response.text
    return html

def getName(html):
    """根据网页内容获取书名"""
    regex_name = '<h1>(.*?)</h1>'
    name = re.findall(regex_name, html)
    return name[0]

def getChapterUl(html):
    """获取章节列表ul """
    regex_catalog_div = '<h4>.*?</h4>\n</div>\n<div class="bd">(.*?)</div>'
    catalog_div = re.findall(regex_catalog_div, html, re.S)
    return catalog_div[1]

def getChapter(catalog_div, name):
    """获取章节名称及地址 """
    regex_catalog = '<li><a href="(.*?)">(.*?)</a></li>'
    catalogs = re.findall(regex_catalog, catalog_div)
    with open(name + '_catalog.txt', 'a', encoding='utf-8') as f:
        for catalog in catalogs:
            f.write(catalog[1])
            f.write('\n')
    return catalogs

def getNextPageUrl(html, presentUrl):
    """获取下一页地址 """
    regex_next_page = '<a class="nextPage" href="(.*?)">下页</a>'
    next_page = re.findall(regex_next_page, html)
    if next_page[0] in presentUrl:
        return ""
    else:
        return next_page[0]

def getContentPage(content_url):
    """获取章节内的页数地址 """
    html = getHtmlByUrl(content_url)
    regex_pages = '<center class="chapterPages">(.*?)</center>'
    pages = re.findall(regex_pages, html)
    regex_page = 'href="(.*?)"'
    page = re.findall(regex_page, pages[0])
    return page

def getContent(pages, base, name, chapter):
    """获取章节内容并写入文件 """
    print('Start: ' + chapter)
    with open(name + '.txt', 'a', encoding='utf-8') as f:
        f.write(chapter + '\r\n')
    for page in pages:
        # print('Start: ' + base + page)
        html = getHtmlByUrl(base + page)
        regex_content = '<div class="page-content font-large">\n<p>(.*?)</p>'
        content = re.findall(regex_content, html, re.S)
        if len(content) > 0:
            content = content[0].replace('<br />', '')
            content = content.replace('&nbsp;', '')
            content = content.replace('\r', '')
            with open(name + '.txt', 'a', encoding='utf-8') as f:
                f.write(content + '\r\n')
        # print('Over: ' + base + page)
    print('Over: ' + chapter)

book_url = "https://www.diyibanzhu4.com/9/9936/"
catalog_base_url = book_url
prefix = 'https://www.diyibanzhu4.com'
html = getHtmlByUrl(book_url)
name = getName(html)
page = 1
next_page = getNextPageUrl(html, book_url)
while next_page != "":
    print("正在抓取第%d页" % page)
    html = getHtmlByUrl(book_url)
    chapter_ul = getChapterUl(html)
    chapters = getChapter(chapter_ul, name)
    for chapter in chapters:
        content_pages = getContentPage(prefix + chapter[0])
        getContent(content_pages, catalog_base_url, name, chapter[1])
    next_page = getNextPageUrl(html, book_url)
    print("抓取完成第%d页" % page)
    if next_page != "":
        book_url = prefix + next_page
        page += 1
    else:
        print("Over")
        break

print('------------Over----------')