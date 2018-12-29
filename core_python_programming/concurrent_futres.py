from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
import requests

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://amazon.com/dp/'
ISBNs = {
    '0132269937':   'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    with requests.get('{}{}'.format(AMZN,isbn)) as page:
        data = page.text
        print(data)
        return str(REGEX.findall(data)[0])#'haven't match any thing but it worked once,mybe the amzon have some rules'

def _main():
    print('At {},on amazon'.format(ctime()))
    with ThreadPoolExecutor(3) as executor:
        for isbn , ranking in zip(ISBNs,executor.map(getRanking,ISBNs)):
            print('- %r rankend %s' % (ISBNs[isbn],ranking))

    print('all done at:',ctime())

if __name__=='__main__':
    _main()
