import requests
import os
import re

def getHtmlByUrlAndPro(url, encode='gbk'):
    """使用代理访问, 需要安装pip install -U requests[sock]"""
    proxies = {
    'https:': 'https://127.0.0.1:1080',
    'http:': 'http://127.0.0.1:1080'
    }
    print(proxies)
    print(url)
    response = requests.get(url, proxies=proxies, timeout=5)
    response.encoding = encode
    return response.text


def getHtmlByUrl(url, encode='gbk'):
    """根据url获取html内容"""
    response = requests.get(url)
    response.encoding = encode
    html = response.text
    return html

def deleteFile(path):
    """根据路径删除文件"""
    if os.path.exists(path):
        os.remove(path)
        print('delete: ' + path)
    else:
        print(path + ",文件不存在！")

def parse(content, regex):
    """根据内容，用正则解析，并返回解析结果"""
    result = re.findall(regex, content, re.S)
    return result

def makeDir(path):
    if os.exists(path):
        pass

def saveFile(path, content, mold='wb'):
    """根据路径与写入方式写入文件"""
    dir_save = path.rsplit('\\', 1)[0]
    if not os.path.exists(dir_save):
        os.makedirs(dir_save)
    with open(path, mold) as f:
        f.write(content)


if __name__ == '__main__':
    pass