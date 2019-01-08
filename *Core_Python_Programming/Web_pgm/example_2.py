# 爬虫解析Web客户端.

from HTMLparser import HTMLparser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin

from Beautifrlsoup import BeautifulSoup,SoupStrainer
from htmlSlib import parse,treebuilders

URLs =(
    'http://python.org',
    'http://google.com',
)
def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url,f):
    'simpleBS() - use BeautifulSoup to parse all tags to get anchors'
    output(urljoin(url,x['href']) for x in BeautifulSoup(f).fidAll('a'))

def fasterBs(url,f):
    'fasterBS() - use BeautifulSoup to parse only anchor tags'
    output(urljoin(url,x['href']) for x in
    BeautifulSoup(f,parseOnlyThese = SoupStrainer('a')))

def htmlparser(url,f):
    'htmlparsr() - use HTML Parser to parse anchor tags'
    class AnchorParser(HTMLparser):
        def handle_starttag(self,tag,attrs):
            if tag !='a':
                return
            if not hasattr(self,'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url,x) for x in parser.data)

def htmlSlibparse(url,f):
    'htmlSlibparse() - use htmlSlib to parse anchor tags'
    output(urljoin(url,x.attributes['href']))
        for x in parse(f) if ininstance(x,treebuilders.simpletree.Element)
        and x.name == 'a')

def process(url,data):
    print('\n*** simple BS')
    simpleBS(url,data)
    data.seek(0)
    print('\n***faster BS')
    fasterBs(url,data)
    data.seek(0)
    print('\n ***HTMLparser')
    htmlparser(url,data)
    data.seek(0)
    print('\n*** HTML5lib')
    html5libparse(url,data)

def main():
    for url in URLs:
        f = urlopen(url)
        data = StingIO(f.read())
        f.close()
        process(url,data)

if __name__ == '__main__':
    main()
    
