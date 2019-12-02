# -*- encding: utf-8 -*-

import requests
import os
import re
import platform
import sys
import json


def isNull(result):
    """判断是否为空，如果为空，则退出程序"""
    if result == None or len(result) < 1:
        print("result 为空")
        sys.exit()


def getBaseDir():
    """获取下载文件夹路径"""
    if platform.system() == 'Windows':
        return 'E:\\fiction\\'
    else:
        return '/home/heyefu/fiction/'


def getHtmlByUrlAndPro(url, encode='gbk'):
    """使用代理访问, 需要安装pip install -U requests[sock]"""
    proxies = {
        'https:': 'https://127.0.0.1:1080',
        'http:': 'http://127.0.0.1:1080'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    response = requests.get(url, proxies=proxies, headers=headers)
    if encode is not None:
        response.encoding = encode
    return response.text


def getFileSeparate():
    """获取文件夹分隔符"""
    if platform.system() == 'Windows':
        return '\\'
    else:
        return '/'


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


def saveFile(path, content, mold='wb', encoding='utf-8'):
    """根据路径与写入方式写入文件"""
    dir_save = path.rsplit(getFileSeparate(), 1)[0]
    if not os.path.exists(dir_save):
        os.makedirs(dir_save)
    if encoding == None:
        with open(path, mold) as f:
            f.write(content)
    else:
        with open(path, mold, encoding=encoding) as f:
            f.write('\n\n')
            f.write(content)


def coverPicToJson(content):
    """将图片转化为json"""
    regex = '<img src="/toimg/data/(.*?)\\.png" />'
    result = parse(content, regex)
    for key in result:
        if key in picDicts:
            content = content.replace('<img src="/toimg/data/' +
                                      key + '.png" />', picDicts[key])
            pass
        else:
            picDicts[key] = ''
    with open('picDicts.json', 'w', encoding='utf-8') as f:
        json.dump(picDicts, f)
    return content


if __name__ == '__main__':
    path = sys.argv[0]
    path = path[:path.rindex('/')]
    with open(path + '/picDicts.json', 'r', encoding='utf-8') as f:
        picDicts = json.load(f)
    with open('E:\\fiction\\txt\\2.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        content = coverPicToJson(content)
    with open('E:\\fiction\\txt\\3.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    pass
