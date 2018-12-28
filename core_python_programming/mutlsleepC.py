import threading,time

loops = [4,2]

class ThreadFunc():
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)#

def loop(nloop,nsec):
    print('start loop',nloop,' at:',time.ctime())
    time.sleep(nsec)
    print('loop',nloop,'don at:',time.ctime())

def main():
    print('staring at:',time.ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(
        target=ThreadFunc(loop,(i,loops[i]),loop.__name__)
        )
        threads.append(t)

    for i in nloops:threads[i].start()
    for i in nloops:threads[i].join()
    print('All loops dont at',':',time.ctime())

main()
