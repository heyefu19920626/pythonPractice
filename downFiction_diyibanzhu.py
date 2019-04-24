import requests
import json
import re
import os


BASE_DIR = 'E:\\fiction\\'


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

def getAuthor(html):
    regex_author = '<p class="info">\n作者：(.*?)<br />'
    author = re.findall(regex_author, html)
    return author[0]

def getChapterUl(html):
    """获取章节列表ul """
    regex_catalog_div = '<h4>.*?</h4>\n</div>\n<div class="bd">(.*?)</div>'
    catalog_div = re.findall(regex_catalog_div, html, re.S)
    return catalog_div[1]

def getChapter(catalog_div, name):
    """获取章节名称及地址 """
    regex_catalog = '<li><a href="(.*?)">(.*?)</a></li>'
    catalogs = re.findall(regex_catalog, catalog_div)
    with open(name, 'a', encoding='utf-8') as f:
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
    if len(pages) < 1:
        return content_url
    regex_page = 'href="(.*?)"'
    page = re.findall(regex_page, pages[0])
    return page

def getContent(pages, base, name, chapter):
    """获取章节内容并写入文件
    pages: 每页的地址数组
    base: 页数的前缀，加上pages中的地址为该页地址
    name: 保存的本地文件名称
    chapter: 章节名
     """
    print('Start: ' + chapter)
    with open(name, 'a', encoding='utf-8') as f:
        f.write(chapter + '\r\n')
    if isinstance(pages,str):
        pages = pages.replace(base, '')
        pages = [pages]
    for page in pages:
        html = getHtmlByUrl(base + page)
        regex_content = '<div class="page-content font-large">\n<p>(.*?)</p>'
        content = re.findall(regex_content, html, re.S)
        if len(content) > 0:
            content = content[0].replace('<br />', '')
            content = content.replace('&nbsp;', '')
            content = content.replace('\r', '')
            content = content.replace("更'多'精'彩'小'说'尽'在'ｗ'ｗ'ｗ．０'１'Ｂ'ｚ．ｎ'Ｅ'ｔ第'一'版'主'小'说'站", '')
            with open(name, 'a', encoding='utf-8') as f:
                f.write(content + '\r\n')
        else:
            print('-----------抓取内容出错-----------')
    print('Over: ' + chapter)


book_url = "https://www.diyibanzhu4.com/3/3550/"
catalog_base_url = book_url
prefix = 'https://www.diyibanzhu4.com'
html = getHtmlByUrl(book_url)
name = getName(html)
author = getAuthor(html)
page = 1
local_name = '《' + name + '》作者：' + author
next_page = getNextPageUrl(html, book_url)
catalog_file = BASE_DIR + 'txt\\' + name + '_catalog.txt'
content_file = BASE_DIR + 'txt\\' + local_name + '.txt'
if os.path.exists(catalog_file):
    os.remove(catalog_file)
    print('delete:' + catalog_file)
if os.path.exists(content_file):
    os.remove(content_file)
    print('delete:' + content_file)

while next_page != "":
    print("正在抓取第%d页" % page)
    html = getHtmlByUrl(book_url)
    chapter_ul = getChapterUl(html)
    chapters = getChapter(chapter_ul, catalog_file)
    for chapter in chapters:
        content_pages = getContentPage(prefix + chapter[0])
        getContent(content_pages, catalog_base_url, content_file, chapter[1])
    next_page = getNextPageUrl(html, book_url)
    print("抓取完成第%d页" % page)
    if next_page != "":
        book_url = prefix + next_page
        page += 1
    else:
        print("Over")
        break

print('------------Over----------')