'''
CREATE TABLE 'wikipedia'.'pages'(
    'id' INT NOT NULL AUTO_INCREMENT,
    'url' VARCHAR(225) NOT NULL,
    'created' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ('id'));

CREATE TABLE 'wikipedia'.'links'(
    'id' INT NOT NULL AUTO_INCREMENT,
    'fromPageId' INT NULL,
    'toPageId' INT NULL,
    'created' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ('id'));

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd=None,
    db='mysql',charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def insertpageifnotexists(url):
    cur.execute('SELECT * FROM pages WHERE url ={}'.format(url))
    if cur.rowcount ==0:
        cur.execute('INSERT INTO PAGES (url) VALUES(%s)' % url)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId,toPageId):
    cur.execute('SELECT *FROM links WHERE fromPageId = %s and \
        toPageId = %s' (int(fromPageId),int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links(fromPageId,toPageId) \
        VALUES(%s,%s)'(int(fromPageId),int(toPageId)))
        conn.commit()

pages = set()
def getLinks(pageurl,recursionlevel):
    global pages
    if recursionlevel > 4:
        return
    pageid = insertpageifnotexists(pageurl)
    html = urlopen('http://en.wikipedia.org'+pageurl)
    bsobj = BeautifulSoup(html)
    for link in bsobj.findAll('a',href=re.compile('^/wiki/((?!:).)*')):
        insertLink(pageId,insertpageifnotexists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            pages.add(newpage)
            getLinks(newpage,recursionlevel+1)

getLinks('/wiki/Kevin_Bacon',0)
cur.close()
conn.close()
