from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,requests

pages = set()
def getLinks(pageUrl):
    global pages
    html = requests.get('http://en.wikipedia.org' + pageUrl).text
    bsObj = BeautifulSoup(html)
    try:
        print('title  '+bsObj.h1.get_text())
        print('content   '+bsObj.find(id='mw-content-text').find('p').get_text())
        print('edit  '+bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("don't worry,just somepages miss some attrs")

    for link in bsObj.findAll('a',href=re.compile('^/wiki/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('---------\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')
