import requests
import re

uid = 4787



# response = requests.get(url)

cookies = {}
cookie = 'VZ7s_2132_saltkey=Vog0gmR0; VZ7s_2132_lastvisit=1528586353; UM_distinctid=163e71804d5b36-0b0e500862cfa2-3c3c5b0b-15f900-163e71804d66d8; VZ7s_2132_ulastactivity=f5d8fjRCJv74E4bDk6g5mNm7vwPmXVJE1vNXAf0DZIi89ymxX3pk; VZ7s_2132_auth=a737cmpU5TIa2uBpSLTzroz6z50O7EPIOwtZHOJHoPZlVdYJuOWZiSNawP9SvfC6B35%2BdOlwBZrGclZR5q3apor6; VZ7s_2132_lastcheckfeed=2506%7C1528590004; VZ7s_2132_smile=4D1; VZ7s_2132_visitedfid=2D39D38D36; VZ7s_2132_atarget=1; VZ7s_2132_st_t=2506%7C1528596536%7C78945cc4cb0165e2759f6eb5039445ab; VZ7s_2132_forum_lastvisit=D_39_1528590167D_38_1528592812D_2_1528596536; CNZZDATA1259871877=1805243662-1528590502-%7C1528600027; VZ7s_2132_noticeTitle=1; VZ7s_2132_viewid=tid_4479; VZ7s_2132_sid=fZEJz7; VZ7s_2132_lip=222.175.126.39%2C1528602224; VZ7s_2132_lastact=1528602239%09forum.php%09viewthread; VZ7s_2132_st_p=2506%7C1528602239%7C47804bcd0a7b62db095a6488f3266bcf'
for line in cookie.split(';'):
    key, value = line.split('=', 1)
    # print(key, value)
    cookies[key] = value
# print(requests.get(url2, cookies=cookies))


index = 1
num = 1

# https://www.xibixibi.com/forum.php?mod=viewthread&tid=4479&extra=page%3D1%26filter%3Dtypeid%26typeid%3D11
while uid < 5000:
    print('正在抓取:uid = ' + str(uid))
    url = 'https://www.xibixibi.com/forum.php?mod=viewthread&tid=' + \
        str(uid) + '&extra=page%3D1%26filter%3Dtypeid%26typeid%3D11'
    try:
        response = requests.get(url, cookies=cookies)
    except:
        if num < 4:
            print('第' + str(num) + '次抓取' + str(uid) + '出错，重新抓取')
            num += 1
            continue
        with open('出错.txt', 'a', encoding='utf-8') as f:
            f.write('抓取' + str(uid) + '出错,不再抓取\n')
        print('抓取' + str(uid) + '出错,不再抓取')
        uid += 1
        num = 1
        continue
    response.encoding = 'utf-8'
    result = response.text
    with open('pic.html', 'w', encoding='utf-8') as f:
        f.write(result)
    # reg_address = r'百度网盘：<div class="showhide".*?链接: <a href="(.*?)" target="_blank">.*?密码:(.*?)</div></td></tr></table>'
    # reg_address = r'<h4>本贴仅VIP可见的内容</h4> 链接：<a href="(.*?)" target="_blank">.*?</a> 密码：(.*?) </div></td></tr></table>'
    reg_address = r'<a href="http.?://pan.baidu.com/s/.*?" target="_blank">(.*?)</a> 密码.?\s?(.{4})'
    reg_title = r'<!-- <span id="thread_subject">(.*?)</span> -->'
    address = re.findall(reg_address, result)
    title = re.findall(reg_title, result)
    print(address)
    print(title)
    if(len(address) < 1):
        if index < 4:
            print(str(uid) + '第' + str(index) + '次未抓取到,重新抓取')
            index += 1
            continue
        with open('出错.txt', 'a', encoding='utf-8') as f:
            f.write(str(uid) + '未抓取到,不再抓取\n');
        print(str(uid) + '未抓取到,不再抓取')
        uid += 1
        index = 1
        continue
    for site in address:
        if len(site) > 1:
            with open('地址.txt', 'a') as f:
                title = 'UID:' + str(uid) + " 标题：" + title[0] + '\n'
                location = "百度网盘：" + site[0] + ' 密码：' + site[1] + '\n'
                f.write(title + location)
    # if len(address[0]) > 1:
    #     with open('地址.txt', 'a') as f:
    #         title = 'UID:' + str(uid) + " 标题：" + title[0] + '\n'
    #         address = "百度网盘：" + address[0][0] + ' 密码：' + address[0][1] + '\n'
    #         f.write(title + address)
    index = 1
    num = 1
    uid += 1
