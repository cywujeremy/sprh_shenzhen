from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote
from fake_useragent import UserAgent
import time
import random
import requests
import string
import logging

def htmlIntoSoup(url, use_agents=False):
    """fetch html and transform into BeautifulSoup objects from specified url

    Args:
        url (str): a string of url

    Returns:
        object (BeautifulSoup): parsed object from the downloaded html
    """
    
    url = quote(url, safe=string.printable)
    time.sleep(random.random() * 10)
    
    # hard-coded fake agents, may need to renew
    # TODO: establish dynamic fake agent pool to avoid hard-coding
    headers = {'User-Agent': UserAgent(verify_ssl=False).random}
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
    
    if use_agents:
    
        proxy = random.choice(proxy_list)
        httpproxy_handler = request.ProxyHandler(proxy)
        opener = request.build_opener(httpproxy_handler)
        req = request.Request(url=url, headers=headers)
        response = opener.open(req)
        soup = BeautifulSoup(response.read(), 'lxml')
    
    else:
        
        response = requests.get(url=url, headers=headers)
        response.encoding = 'GB2312'
        soup = BeautifulSoup(response.text, 'lxml')       
    
    return soup