import math
import json
import requests
import logging

# constants
x_pi = math.pi * 3000.0 / 180.0
pi = math.pi
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率

def gcj02_to_wgs84(lng, lat):
    """GCJ02(火星坐标系)经纬度转GPS84经纬度
    
    Args:
        lng (float): longitude in GCJ02 projection
        lat (float): latitude in GCJ02 projection
        
    Returns:
        (tuple): GPS/WGS84 longitude and latitude
    """

    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    
    return lng * 2 - mglng, lat * 2 - mglat

def _transformlat(lng, lat):
        
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    
    return ret

def _transformlng(lng, lat):
        
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    
    return ret

def getGeoCode(searchLocation, city='深圳市', key='75450f9014e6e0800f5c479088bc0b76'):
    
    """obtain the geo-encoding (latitude and longitude) of the specified location using Amap API

    Args:
        searchLocation (str, in Chinese): the address of the location
        city (str, in Chinese): the name of the city to be searched
        key (str): the Amap API key -- REPLACE IT WITH YOUR OWN ONE -- THE DEFAULT ONE MAY NOT WORK.

    Returns:
        tuple with structure (lat, lng)
    """
    
    api_addr = f"https://restapi.amap.com/v3/geocode/geo?address={searchLocation}&city={city}&output=json&key={key}"
    req = requests.get(api_addr)
    content = req.content
    sjson = json.loads(content)
    
    if sjson['status'] == '1':
        
        try:
            return sjson['geocodes'][0]['formatted_address'], sjson['geocodes'][0]['location']
        
        except IndexError and TypeError:
            logging.debug(f'{searchLocation}-查询不到坐标')
            return 'error', 'error'
        
    else:
        
        return 'error', 'error'