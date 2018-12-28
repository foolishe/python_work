import threading,time


loops = [4,2]

def loop(nloop,nsec):
    print('Start loop:',nloop,'at',time.ctime())
    time.sleep(nsec)
    print('loop',nloop,'done at:',time.ctime())

def main():
    print('starting at',time.ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(nloops[i],loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    # for i in nloops:
        threads[i].join()
    print('All loops done at:',time.ctime())

if __name__=='__main__':
    main()
