import requests
from bs4 import BeautifulSoup
import openpyxl as op
import time
import random
from urllib import request
from urllib.parse import quote
import string
from fake_useragent import UserAgent


def htmlIntoSoup(url):
    url = quote(url, safe=string.printable)
    time.sleep(random.random() * 10)
    headers = {
        'User-Agent': UserAgent(verify_ssl=False).random}
    proxy_list = [
        {'http': '115.29.170.58:8118'},
        {'http': '117.88.5.211:3000'},
        {'http': '222.95.240.228:3000'},
        {'http': '121.237.149.54:3000'},
        {'http': '117.88.5.126:3000'},
        {'http': '121.237.149.141:3000'},
        {'http': '222.95.241.123:3000'},
        {'http': '117.62.173.31:8118'},
        {'http': '117.88.5.15:3000'},
        {'http': '117.88.176.188:3000'},
        {'http': '60.190.250.120:8080'},
        {'http': '222.95.241.236:3000'},
        {'http': '222.95.144.46:3000'},
        {'http': '117.88.5.105:3000'},
        {'http': '222.95.144.72:3000'},
        {'http': '121.237.148.216:3000'},
        {'http': '117.88.4.91:3000'},
        {'http': '222.95.241.243:3000'},
        {'http': '106.122.205.36:8118'},
        {'http': '180.118.252.180:8118'},
        {'http': '121.237.149.158:3000'},
        {'http': '114.233.201.7:8118'},
        {'http': '117.87.180.144:8118'},
        {'http': '222.95.144.246:3000'},
        {'http': '117.88.177.86:3000'},
        {'http': '117.88.177.139:3000'},
        {'http': '121.237.148.195:3000'},
        {'http': '117.88.4.36:3000'},
        {'http': '117.88.4.55:3000'},
        {'http': '121.237.149.189:3000'},
        {'http': '117.88.176.176:3000'},
        {'http': '121.237.149.86:3000'},
        {'http': '117.85.166.121:8118'},
        {'http': '117.88.4.215:3000'},
        {'http': '121.237.149.180:3000'},
        {'http': '117.88.4.20:3000'},
        {'http': '117.88.176.213:3000'},
        {'http': '117.88.176.99:3000'},
        {'http': '121.237.149.62:3000'},
        {'http': '183.167.217.152:63000'},
        {'http': '117.88.5.167:3000'},
        {'http': '119.254.94.71:42788'},
        {'http': '117.88.176.169:3000'},
        {'http': '121.237.148.130:3000'},
        {'http': '121.237.148.228:3000'},
        {'http': '117.94.213.117:8118'},
        {'http': '121.237.149.16:3000'},
        {'http': '121.237.149.75:3000'},
        {'http': '121.237.148.151:3000'},
        {'http': '117.88.5.147:3000'},
        {'http': '117.88.177.3:3000'},
        {'http': '222.95.144.71:3000'},
        {'http': '14.212.249.10:8118'},

    ]
    proxy = random.choice(proxy_list)
    httpproxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(httpproxy_handler)
    req = request.Request(url=url, headers=headers)
    response = opener.open(req)
    soup = BeautifulSoup(response.read(), 'lxml')
    return soup


def htmlIntoSoup_normal(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'GB2312'
    #processedtexts = response.text.replace('\r', '')
    processedtexts = response.text.replace('\r\n', '')
    soup = BeautifulSoup(processedtexts,'lxml')
    return soup


def getINFO(schoolitem):
    try:
        name = schoolitem.dd.find(class_='title').a.text
    except Exception:
        name = 'error'
    try:
        address = schoolitem.dd.find(class_='gray6 mt13').text
    except Exception:
        address = 'error'
    try:
        attr = schoolitem.dd.find(class_='mt15').text
    except Exception:
        attr = 'error'
    return [name, address, attr]


def writeINFO():
    wb = op.load_workbook("D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.03/深圳市学校层次.xlsx")
    ws1 = wb['URL']
    ws2 = wb['INFO']
    i = 1
    while i <= ws1.max_row:
        tag = htmlIntoSoup_normal(ws1['A' + str(i)].value).find(class_="schoollist").contents
        for item in tag:
            if item != ' ':
                iteminfo = getINFO(item)
                ws2.append(getINFO(item))
                print(iteminfo[0]+' success!')
        i += 1
    wb.save("D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.03/深圳市学校层次.xlsx")


if __name__ == '__main__':
    #demo_tag = htmlIntoSoup_normal('https://sz.esf.fang.com/school/').find(class_="schoollist")
    #print(demo_tag.contents[1].dd.find(class_='mt15').text)
    writeINFO()
