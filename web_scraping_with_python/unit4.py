from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div',{'id':'bodyContent'}).findAll('a',
        href=re.compile('^/wiki/((?!:).)*'))
def getHistoryIPs(pageurl):
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=getHistoryIPs
    pageurl = pageurl.replace('/wiki/','')
    historyUrl = 'http://en.wikipedia.org/w/index.php?\
        title='+pageurl+'&action=history'
    print('history url is: '+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipAddresses = bsObj.findAll('a',{'class':'mw-userlink mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks('wiki/python_(programming_language)')
while(len(links) > 0):
    for link in links:
        print('----------')
        HistoryIPs = getHistoryIPs(link.attrs['href'])
        for HistoryIP in HistoryIPs:
            print(HistoryIP)
    newlink = links[random.randrange(len(links)).attrs['href']
    links = getLinks(newlink)

def getcountry(ipaddress):
    try:
        response = urlopen('http://freegeoip.net/json/'+
            ipaddress).read().decode('utf-8')

    except HTTPError:
        return None
    responsejson = json.loads(response)
    return responsejson.get('country_code')
      c 
