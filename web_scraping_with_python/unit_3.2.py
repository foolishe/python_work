from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re,datetime,random,requests

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme + \
        '://' +urlparse(includeUrl).netloc

    internalLinks = set()
    for link in bsObj.findAll('a',href=re.compile('^(/'+includeUrl+')')):
        if link.attrs['href'] is not None:
            internalLinks.add(link.attrs['href'])
    return list(internalLinks)

def getExternalLinks(bsObj):
    externalLinks = set()
    for link in bsObj.findAll('a',
        href=re.compile('^(http|www)')):
        if link.attrs['href'] is not None:
            externalLinks.add(link.attrs['href'])
        return list(externalLinks)

def getRandomExternalLink(startingPage):
    html = requests.get(startingPage).text
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage))
    if len(externalLinks) == 0:
        print('No external links,looking around the site for one')
        internalLinks = getInternalLinks(startingPage)
        return getExternalLinks(internalLinks[random.randrange(len(internalLinks))])
    else:
        return externalLinks[random.randrange(len(externalLinks))]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is :'+externalLink)
    followExternalOnly(externalLink)

url = 'http://socialmediasite.com/api/v4/json/users/1234/posts?from=08012014&to=08312014'
print(urlparse(url))
