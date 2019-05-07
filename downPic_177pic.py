import requests

from down_basic import getHtmlByUrl as getHtmlByUrl
from down_basic import parse as parse
from down_basic import saveFile as saveFile

BASE_DIR = 'E:\\down\\'

def getName(html):
    """获取漫画名称"""
    name = '<h1 class="entry-title">(.*?)</h1>'
    name = parse(html, name)
    return name[0]

def getPicNum(html):
    """获取图片数量"""
    pic_num = '<title>.*\\[(\\d+)P\\].*</title>'
    pic_num = parse(html, pic_num)
    return pic_num[0]

def getPicUrl(html):
    """根据网页获取图片地址"""
    pic_url = '<p><img src="(.*?)".*?class="alignnone.*?" /></p>'
    pic_url = parse(html, pic_url)
    return pic_url

def getNextPage(html):
    """获取下一页地址，如果没有，返回None"""
    next_url = '<div class="wp-pagenavi">.*<a href="(.*?)">下一页</a>'
    next_url = parse(html, next_url)
    if len(next_url) > 0:
        return next_url[0]
    else:
        return None

def getPicName(num, total):
    """获取图片名称"""
    num = str(num)
    minus = len(total) - len(num)
    if minus > 0:
        num = '0' * minus + num
        return num

def downCartoon(url):
    html = getHtmlByUrl(url, encode='utf-8')
    name = getName(html)
    print('Down:' + name + '......')
    save_path = BASE_DIR + name + '\\'
    total_num = getPicNum(html)
    print('共%s副图' % total_num)

    num = 1
    next_page = True
    print('下载第1页中...')
    while next_page != None:
        pic_urls = getPicUrl(html)
        suffix = pic_urls[0].rsplit('.', 1)[1]
        for pic_url in pic_urls:
            print('下载%d中...' % num)
            response = requests.get(pic_url)
            data = response.content
            saveFile(save_path + getPicName(num, total_num) + '.' + suffix, data)
            num += 1
        next_page = getNextPage(html)
        if next_page != None:
            page = next_page.rsplit('/', 1)[1]
            print('下载第%s页中' % page)
            html = getHtmlByUrl(next_page, 'utf-8')


# url = 'http://www.177pic.info/html/2015/06/60390.html'
# url = 'http://www.177pic.info/html/2019/05/2869138.html'
url = 'http://www.177pic.info/html/2019/05/2898524.html'
# html = getHtmlByUrl(url, 'utf-8')
# print(getNextPage(html))
downCartoon(url)
