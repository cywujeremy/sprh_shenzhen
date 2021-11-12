# coding:utf-8
import xlrd
import xlwt
import requests
import urllib
import math
import re

pattern_x = re.compile(r'"x":(".+?")')
pattern_y = re.compile(r'"y":(".+?")')


def mercator2wgs84(mercator):        
    """translate coordinates in Mercator projection to WGS84 projection
    
    Args:
        mercator (tuple): a tuple with length of 2 indicating longitude and latitude
        
    Returns:
        x, y (float): a tuple of translated longitude and latitude
    """
    
    point_x = mercator[0]
    point_y = mercator[1]
    x = point_x / 20037508.3427892 * 180
    y = point_y / 20037508.3427892 * 180
    y = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180)) - math.pi / 2)
    
    return x, y


def get_mercator(addr):
    """obtain coordinates in Mercator projection for specified address from Baidu Map API

    Args:
        addr (str): a string of the address

    Returns:
        location (tuple): a tuple with length of 2 indicating longitude and latitude
    """
    quote_addr = urllib.parse.quote(addr.encode('utf8')) #编码转码
    city = urllib.parse.quote(u'深圳市'.encode('utf8'))
    province = urllib.parse.quote(u'广东省'.encode('utf8'))
    
    if quote_addr.startswith(city) or quote_addr.startswith(province):
        pass
    else:
        quote_addr = quote_addr
        
    s = urllib.parse.quote(u'深圳市'.encode('utf8'))
    api_addr = "http://api.map.baidu.com/?qt=gc&wd=%s&cn=%s&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk62300" % (
        quote_addr, s)
    req = requests.get(api_addr)
    content = req.text
    x = re.findall(pattern_x, content)
    y = re.findall(pattern_y, content)
    
    if x:
        x = x[0]
        y = y[0]
        x = x[1:-1]
        y = y[1:-1]
        x = float(x)
        y = float(y)
        location = (x, y)
    else:
        location = ()
        
    return location


def _run():
    
    data = xlrd.open_workbook('202003SPRH.xlsx')
    rtable = data.sheets()[0]  # 通过索引顺序获取
    nrows = rtable.nrows  #获取该sheet中的有效行数
    values = rtable.col_values(0)  #返回由该列中所有单元格的数据组成的列表第一个
    workbook = xlwt.Workbook()
    wtable = workbook.add_sheet('202003SPRH经纬度', cell_overwrite_ok=True)
    row = 0
    for value in values:
        value= str(value)
        mercator = get_mercator(value)
        if mercator:
            wgs = mercator2wgs84(mercator)
        else:
            wgs = ('NotFound', 'NotFound')
        print("%s,%s,%s" % (value, wgs[0], wgs[1]))
        wtable.write(row, 0, value)
        wtable.write(row, 1, wgs[0])
        wtable.write(row, 2, wgs[1])
        row = row + 1

    workbook.save('202003SPRH经纬度.xls')


if __name__ == '__main__':
    _run()