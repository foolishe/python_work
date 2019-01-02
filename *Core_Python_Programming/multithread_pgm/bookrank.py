from atexit import register
import re
from threading import Thread
from time import ctime
import requests
import urllib.request

REGEX = '#([\d,]+) in Books'
AMZN = 'https://amazon.com/dp/'
ISBNs = {
'0132269937':'core python programming',
'0132356139': 'python web development with Django',
'0137143419': 'python fundamentals',
}

def getRanking(isbn):
    url=f'{AMZN}{isbn}'
    with requests.get(url) as f:
        return re.findall(REGEX,f.text)[0]
getRanking('0132269931')
# def _showRanking(isbn):
#     print (f'{ISBNs[isbn]} ranked',str(f'{getRanking(isbn)}','utf-8'))
#
# def _main():
#     print(f'At {ctime()},on Amazon...')
#     for isbn in ISBNs:
#         print(isbn)
#         Thread(target=_showRanking,args=(isbn,)).start()

"""“from concurrent.futures import ThreadPoolExecutor
...
def _main():
print('At', ctime(), 'on Amazon...')
with ThreadPoolExecutor(3) as executor:
for isbn in ISBNs:
executor.submit(_showRanking, isbn)
print('all DONE at:', ctime())”

摘录来自: [美]卫斯理 春（Wesley Chun）. “Python核心编程 第3版。” Apple Books.

@register
def _atexit():
    print(f'All done at:{ctime()}')

#urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1051)>
# [Finished in 0.951s]
"""
