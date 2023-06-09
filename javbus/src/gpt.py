from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re


def get_html_content(url, proxy):
    # 设置代理参数
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL",
    }

    # 创建 Chrome WebDriver 实例
    # 启动Chrome浏览器
    driver_path = 'chromedriver.exe'  # 请替换为实际的 chromedriver 路径
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 无界面模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    # 发起带代理的HTTP请求
    driver.get(url)
    html_content = driver.page_source

    # 关闭 WebDriver
    driver.quit()

    return html_content


def extract_code(html_content):
    # 使用正则表达式查找识别码
    pattern = r'<span class="header">識別碼:</span> <span style="color:#CC0000;">(.*?)</span>'
    match = re.search(pattern, html_content)

    if match:
        code = match.group(1)
        return code
    else:
        return None


def extract_release_date(html_content):
    # 使用正则表达式查找发行日期
    pattern = r'<span class="header">發行日期:</span> (.*?)</p>'
    match = re.search(pattern, html_content)

    if match:
        release_date = match.group(1)
        return release_date.strip()
    else:
        return None


def extract_length(html_content):
    # 使用正则表达式查找长度
    pattern = r'<span class="header">長度:</span> (.*?)分鐘</p>'
    match = re.search(pattern, html_content)

    if match:
        length = match.group(1)
        return length.strip()
    else:
        return None


def extract_actors(html_content):
    # 使用正则表达式查找演员
    pattern = r'<div class="star-name"><a href=".*?" title=".*?">(.*?)</a></div>'
    matches = re.findall(pattern, html_content)

    if matches:
        actors = [actor.strip() for actor in matches]
        return actors
    else:
        return None


def print_results(code, release_date, length, actors):
    print("识别码:", code) if code else print("未找到识别码")
    print("发行日期:", release_date) if release_date else print("未找到发行日期")
    print("长度:", length) if length else print("未找到长度")
    if actors:
        print("演员:")
        for actor in actors:
            print(actor)
    else:
        print("未找到演员")


# 示例用法
url = "https://www.javbus.com/ABW-356"
proxy = "http://127.0.0.1:1081"  # 设置代理地址

html_content = get_html_content(url, proxy)
code = extract_code(html_content)
release_date = extract_release_date(html_content)
length = extract_length(html_content)
actors = extract_actors(html_content)

print_results(code, release_date, length, actors)
