from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost',user='root',
    passwd=None,db='mysql',charset='utf8')

cur = conn.cursor()
cur.execute('USE scraping')
random.seed(datetime.datetime.now())

def store(title,content):
    cur.execute('INSERT INTO pages (title,content) VALUES({},{})'
        .format(title,content))

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj = BeautifulSoup(html)
    title = bsObj.find('h1').get_text()
    content = bsObj.find('div',
        {'id':'mw-content-text'}).find('p').get_text()
    store(title,content)
    return bsObj.find('div',{'id':'bodyContent'}).findAll(
        'a',href=re.compile('^/wiki/((?!:).)*')
    )

links = getLinks('wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newarticle = links[random.randrange(len(links))].attrs['href']
        print(newarticle)
        links = getLinks(newarticle)

finally:
    cur.close()
    conn.colse()

    
