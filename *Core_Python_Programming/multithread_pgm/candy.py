from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread
from time import sleep,ctime

lock = Lock()
max = 5
candytray = BoundedSemaphore(max)

def refill():
    lock.acquire()
    print('refilling candy...')
    try:
        candytray.release()
    except ValueError:
        print ('full,skipping')
    else:
        print('ok')
    lock.release()

def buy():
    lock.acquire()
    print('buying candy...')
    if candytray.acquire(False):
        print('ok')
    else:
        print('empty,skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(4))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting at :',ctime())
    nloops = randrange(2,6)
    print('The candy machine (full with %d vars)!' % max)
    Thread(target=consumer,args=(randrange(nloops,nloops+max+10),)).start()
    Thread(target=producer,args=(nloops,)).start()

@register
def _atexit():
    print('All done at:',ctime())

if __name__=='__main__':
    _main()
