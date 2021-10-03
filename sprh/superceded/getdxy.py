import requests
from bs4 import BeautifulSoup
import openpyxl as op


def htmlIntoSoup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'GB2312'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def getInfo(soup):
    hospName = soup.find(text='所在区县').parent.parent.previous_sibling.previous_sibling.text
    district = soup.find(text='所在区县').parent.next_sibling.next_sibling.text
    address = soup.find(text='详细地址').parent.next_sibling.next_sibling.text
    attr = soup.find(text='性质').parent.next_sibling.next_sibling.text
    level = soup.find(text='级别').parent.next_sibling.next_sibling.text
    rank = soup.find(text='等级').parent.next_sibling.next_sibling.text
    listed = soup.find(text='是否指定医院').parent.next_sibling.next_sibling.text
    return [hospName, district, address, attr, level, rank, listed]


def writeXlsx():
    wb = op.load_workbook('D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2019.10 深圳/深圳市医院信息.xlsx')
    ws1 = wb['URLs']
    ws2 = wb['INFO']
    i = 2
    while i <= ws1.max_row:
        hospinfo = getInfo(htmlIntoSoup(ws1['A'+str(i)].value))
        ws2.append(hospinfo)
        i += 1
    wb.save('D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2019.10 深圳/深圳市医院信息.xlsx')


if __name__ == '__main__':
    writeXlsx()
