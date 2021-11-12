from utils.scraper import htmlIntoSoup
import openpyxl as op

def getInfo(soup):
    
    hospName = soup.find(text='所在区县').parent.parent.previous_sibling.previous_sibling.text
    district = soup.find(text='所在区县').parent.next_sibling.next_sibling.text
    address = soup.find(text='详细地址').parent.next_sibling.next_sibling.text
    attr = soup.find(text='性质').parent.next_sibling.next_sibling.text
    level = soup.find(text='级别').parent.next_sibling.next_sibling.text
    rank = soup.find(text='等级').parent.next_sibling.next_sibling.text
    listed = soup.find(text='是否指定医院').parent.next_sibling.next_sibling.text
    
    return hospName, district, address, attr, level, rank, listed


def writeXlsx(wb_path):
    
    wb = op.load_workbook(wb_path)
    ws1 = wb['URLs']
    ws2 = wb['INFO']
    i = 2
    
    while i <= ws1.max_row:
        hospinfo = getInfo(htmlIntoSoup(ws1['A'+str(i)].value))
        ws2.append(hospinfo)
        i += 1
        
    wb.save(wb_path)


if __name__ == '__main__':
    writeXlsx()
