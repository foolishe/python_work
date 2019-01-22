from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime,random,re,requests

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = requests.get('http://en.wikipedia.org'+articleUrl).text
    bsObj = BeautifulSoup(html)
    return bsObj.find('div',{'id':'bodyContent'}).findAll(
        'a',href=re.compile('^/wiki/((?!:).)*')
    )
Links = getLinks('/wiki/Kevin_Bacon')
while len(Links) < 0:
    newArticle = Links[random.randrange(len(Links))].attrs['href']
    print(
        '====================\n',
        newArticle
    )
    Links = getLinks(newArticle)

pages = set()
def getlinks(pageUrl):
    global pages
    html = requests.get('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html.text)
    for link in bsObj.findAll('a',href=re.compile('^/wiki/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getlinks(newPage)

getlinks('')
