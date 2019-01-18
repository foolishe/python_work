'''标签对象,findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)”

摘录来自: [美] Ryan Mitchell. “Python网络数据采集。” Apple Books. '''

'NavigableString: 获取标签里面的文字'
'comment: 查找注释标签'

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests

def getTitle(url):
    try:
        html = requests.get(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.text)
        title = bsObj.findAll('script')
    except AttributeError as e:
        return None
    return title

url = ['http://www.pythonscraping.com','http://www.weibo.com']
title = getTitle(url[1])
if title == None:
    print('Title could not be found')
else:
    print(title)
