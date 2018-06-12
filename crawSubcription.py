import requests
import json
import re


cookies = {}
cookie = 'sessionid=a9211c8245823ed0f8940000; steamCountry=CA%7C0d62e1154491d414344cab60d0d19ced; _ga=GA1.2.233008569.1528727166; _gid=GA1.2.1531365414.1528727166; timezoneOffset=28800,0; steamLogin=76561198132831432%7C%7C42BEFCD31EB9C848059FB2E97AEE91A7E864298C; steamLoginSecure=76561198132831432%7C%7C68F9C1FB22F2DBC25C0AF741EECD4E70B86163E3; steamMachineAuth76561198132831432=2E94331EBA1E2D45CEDB4324523F7265EA8FB19B'
for line in cookie.split(';'):
    key, value = line.split('=', 1)
    # print(key, value)
    cookies[key] = value

print(cookies)

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
    'Referer': 'https://steamcommunity.com/profiles/76561198132831432/myworkshopfiles/?appid=431960&sort=score&browsefilter=mysubscriptions&view=imagewall&p=1&numperpage=30',
    'Host': 'steamcommunity.com',
    'Cache-Control': 'max-age=0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Upgrade-Insecure-Requests' : '1',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}


page = 1
subcription = {}
while page < 17:
    url = 'https://steamcommunity.com/profiles/76561198132831432/myworkshopfiles/?appid=431960&sort=score&browsefilter=mysubscriptions&view=imagewall&p=' + \
        str(page) + '&numperpage=30'
    print('正在抓取第' + str(page) + '页订阅数据')
    response = requests.get(url, cookies=cookies, headers=headers)
    response.encoding = 'utf-8'
    result = response.text
    # with open('steam.html', 'w', encoding='utf-8') as f:
    #     f.write(result)
    reg_id = r'id=(.*?)"><div class="workshopItemPreviewHolder">'
    reg_tile = r'<div class="workshopItemTitle">(.*?)</div>'
    subcription_id = re.findall(reg_id, result)
    subcription_title =re.findall(reg_tile, result)
    i = 0
    for id in subcription_id:
        subcription[id] = subcription_title[i * 2]
        i += 1
    print(subcription_title)
    page += 1

print(len(subcription))
with open('subcription.json', 'w', encoding='utf-8') as f:
    json.dump(subcription, f, ensure_ascii=False)