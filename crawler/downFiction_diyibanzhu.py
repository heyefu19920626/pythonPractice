# -*- encoding: utf-8 -*-
import json
import re
import sys

import requests
from crawler.down_basic import deleteFile as deleteFile
from crawler.down_basic import parse as parse
from crawler.down_basic import saveFile as saveFile

BASE_DIR = '/Users/tangan/Downloads/fiction'
PIC_DICTS = {}


def get_html_by_url(url, encode='gbk'):
    """根据url获取html内容"""
    response = requests.get(url)
    response.encoding = encode
    html = response.text
    return html


def get_name(html):
    """根据网页内容获取书名"""
    regex_name = '<h1>(.*?)</h1>'
    name = re.findall(regex_name, html)
    return name[0]


def get_author(html):
    regex_author = '<p class="info">\n作者：(.*?)<br />'
    author = re.findall(regex_author, html)
    return author[0]


def get_chapter_ul(html):
    """获取章节列表ul """
    regex_catalog_div = '<h4>.*?</h4>\n</div>\n<div class="bd">(.*?)</div>'
    catalog_div = re.findall(regex_catalog_div, html, re.S)
    return catalog_div[1]


def get_chapter(catalog_div, name):
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


def get_page(html):
    """获取总页数"""
    regex_page = '第(\d+)/(\d+)页'
    page = re.findall(regex_page, html)
    return int(page[0][0]), int(page[0][1])


def get_content_page(content_url):
    """获取章节内的页数地址 """
    html = get_html_by_url(content_url)
    regex_pages = '<center class="chapterPages">(.*?)</center>'
    pages = re.findall(regex_pages, html)
    if len(pages) < 1:
        return content_url
    regex_page = 'href="(.*?)"'
    page = re.findall(regex_page, pages[0])
    return page


def formatter_content(content):
    """格式化内容"""
    content = content.replace('<br />', '\n')
    content = content.replace('&nbsp;', '')
    content = content.replace('&#.{4};', '')
    content = content.replace('\r', '')
    content = covert_pic_to_json(content)
    return content


def covert_pic_to_json(content):
    """将图片转化为json"""
    regex = '<img src="(/toimg/data/(.*?)\\.png)" />'
    result = parse(content, regex)
    prefix = 'https://www.diyibanzhu6.in'
    for res in result:
        key = res[1]
        if key in PIC_DICTS:
            if not str.startswith(PIC_DICTS[key], 'http'):
                content = content.replace('<img src="/toimg/data/' + key + '.png" />', PIC_DICTS[key])
        else:
            PIC_DICTS[key] = prefix + res[0]
    with open('picDicts.json', 'w', encoding='utf-8') as f:
        json.dump(PIC_DICTS, f, ensure_ascii=False)
    return content


def get_content(pages, base, name, chapter):
    """获取章节内容并写入文件
    pages: 每页的地址数组
    base: 页数的前缀，加上pages中的地址为该页地址
    name: 保存的本地文件名称
    chapter: 章节名
     """
    print('Start: ' + chapter)
    with open(name, 'a', encoding='utf-8') as f:
        f.write(chapter + '\r\n')
    if isinstance(pages, str):
        pages = pages.replace(base, '')
        pages = [pages]
    for page in pages:
        html = get_html_by_url(base + page)
        regex_content = '<div class="page-content font-large">\n<p>(.*?)</p>'
        content = re.findall(regex_content, html, re.S)
        if len(content) > 0:
            content = formatter_content(content[0])
            with open(name, 'a', encoding='utf-8') as f:
                f.write(content + '\r\n')
        else:
            print('-----------抓取内容出错-----------')
    print('Over: ' + chapter)


def main(url):
    book_url = url
    catalog_base_url = book_url
    prefix = 'https://www.diyibanzhu6.in'
    html = get_html_by_url(book_url)
    name = get_name(html)
    author = get_author(html)
    page = 1
    local_name = '《' + name + '》作者：' + author
    print(local_name)
    next_page = getNextPageUrl(html, book_url)

    catalog_file = BASE_DIR + '/txt/' + name + '_catalog.txt'
    content_file = BASE_DIR + '/txt/' + local_name + '.txt'
    deleteFile(catalog_file)
    deleteFile(content_file)

    pre_page, total_page = get_page(html)

    # 从第几章开始
    start = 0
    pre = 0

    while pre_page <= total_page:
        print("正在抓取第%d页" % page)
        chapter_ul = get_chapter_ul(html)
        chapters = get_chapter(chapter_ul, catalog_file)
        for chapter in chapters:
            if pre < start:
                pre += 1
                continue
            content_pages = get_content_page(prefix + chapter[0])
            get_content(content_pages, catalog_base_url, content_file, chapter[1])
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
    path = sys.argv[0]
    path = path[:path.rindex('/')]
    with open(path + '/picDicts.json', 'r', encoding='utf-8') as f:
        PIC_DICTS = json.load(f)
    main("https://www.diyibanzhu6.in/14/14247/")
    # book_url = "https://www.diyibanzhu4.com/1/1874/"
    # catalog_base_url = book_url
    # prefix = 'https://www.diyibanzhu4.com'
    # html = getHtmlByUrl(book_url)
    # pre, total = getPage(html)
    # print(pre, total)
