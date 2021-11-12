import requests
import json
import openpyxl as op


def getPOI(api_addr):  # 获取某一页面中的兴趣点
    req = requests.get(api_addr)
    content = req.content
    sjson = json.loads(content)
    infopage = []
    if sjson['status'] == '1':
        for item in sjson['pois']:
            infopage.append(
                [item['id'], item['name'], item['type'], item['typecode'], item['address'], item['location'],
                 item['pname'], item['cityname'], item['adname']])
        return infopage
    else:
        return [['error']]


def writeXLSX():
    wb = op.load_workbook('D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2019.10 深圳/深圳市公园信息.xlsx')
    ws = wb['Sheet1']
    prerequest = json.loads(requests.get(
        "https://restapi.amap.com/v3/place/text?keywords=公园&types=110100&city=shenzhen&citylimit=true&output=json&offset=20&page=1&key=75450f9014e6e0800f5c479088bc0b76").content)
    count = int(prerequest['count'])
    pagenumber = (count // 20) + 1
    for i in range(1, pagenumber + 1):
        api_addr = "https://restapi.amap.com/v3/place/text?keywords=公园&types=110100&city=shenzhen&citylimit=true&output=json&offset=20&page=" + str(i) + "&key=75450f9014e6e0800f5c479088bc0b76"
        pageinfo = getPOI(api_addr)
        for item in pageinfo:
            try:
                ws.append(item)
            except Exception:
                ws.append(['error'])
        wb.save('D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2019.10 深圳/深圳市公园信息.xlsx')

if __name__ == '__main__':
    writeXLSX()