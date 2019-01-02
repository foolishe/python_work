from atexit import register
from random import randrange
from threading import Thread,Lock,currentThread
from time import sleep,ctime

class ClearOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)

lock = Lock()
loops = (randrange(2,6) for x in range(randrange(3,1\)))
remaining = ClearOutputSet()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print(f'{myname} Started {ctime()}')
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print(f'{myname} completed at:{ctime()},spend{nsec}secs')
    print(f' remaining:{remaining}')
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop,args=(pause,)).start()

@register
def _atexit():
    print (f'all done at:{ctime()}')

if __name__=='__main__':
    _main()
