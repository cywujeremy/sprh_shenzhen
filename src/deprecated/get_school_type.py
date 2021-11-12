from utils.scraper import htmlIntoSoup
import openpyxl as op


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
    return name, address, attr


def writeINFO():
    wb = op.load_workbook("D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.03/深圳市学校层次.xlsx")
    ws1 = wb['URL']
    ws2 = wb['INFO']
    i = 1
    while i <= ws1.max_row:
        tag = htmlIntoSoup(ws1['A' + str(i)].value).find(class_="schoollist").contents
        for item in tag:
            if item != ' ':
                iteminfo = getINFO(item)
                ws2.append(getINFO(item))
                print(iteminfo[0]+' success!')
        i += 1
    wb.save("D:/OneDriveLocal/OneDrive/学习/毕业/毕业论文/2020.03/深圳市学校层次.xlsx")


if __name__ == '__main__':
    
    writeINFO()
