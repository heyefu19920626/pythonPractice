import requests
import json
import re
import os
from down_basic import deleteFile as deleteFile
from down_basic import saveFile as saveFile


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
    for catalog in catalogs:
        saveFile(name, catalog[1], 'a')
    return catalogs

def getNextPageUrl(html, presentUrl):
    """获取下一页地址 """
    regex_next_page = '<a class="nextPage" href="(.*?)">下页</a>'
    next_page = re.findall(regex_next_page, html)
    if next_page[0] in presentUrl:
        return ""
    else:
        return next_page[0]

def getPage(html):
    """获取总页数"""
    regex_page = '第(\d+)/(\d+)页'
    page = re.findall(regex_page, html)
    return int(page[0][0]), int(page[0][1])

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

def formatterContent(content):
    """格式化内容"""
    content = content.replace('<br />', '\n')
    content = content.replace('&nbsp;', '')
    content = content.replace('\r', '')
    return content

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
            content = formatterContent(content[0])
            with open(name, 'a', encoding='utf-8') as f:
                f.write(content + '\r\n')
        else:
            print('-----------抓取内容出错-----------')
    print('Over: ' + chapter)

def main(url):
    book_url =  url
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
    deleteFile(catalog_file)
    deleteFile(content_file)

    pre_page, total_page = getPage(html)

    start = 53
    pre = 0

    while pre_page <= total_page:
        print("正在抓取第%d页" % page)
        html = getHtmlByUrl(book_url)
        chapter_ul = getChapterUl(html)
        chapters = getChapter(chapter_ul, catalog_file)
        for chapter in chapters:
            if pre < start:
                pre += 1
                continue
            content_pages = getContentPage(prefix + chapter[0])
            getContent(content_pages, catalog_base_url, content_file, chapter[1])
            pre += 1
        next_page = getNextPageUrl(html, book_url)
        print("抓取完成第%d页" % page)
        if next_page != "":
            book_url = prefix + next_page
            page += 1
        else:
            print("Over")
            break
        pre_page += 1

    print('------------Over----------')
if __name__ == '__main__':
    main("http://www.diyibanzhu4.xyz/1/1874/")
    # book_url = "https://www.diyibanzhu4.com/1/1874/"
    # catalog_base_url = book_url
    # prefix = 'https://www.diyibanzhu4.com'
    # html = getHtmlByUrl(book_url)
    # pre, total = getPage(html)
    # print(pre, total)