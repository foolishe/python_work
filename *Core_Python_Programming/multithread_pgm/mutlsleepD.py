import threading,time

loops = [4,2]

def loop(nloop,nsec):
    print('start loop:','at',time.ctime())
    time.sleep(nsec)
    print('loops','at',':',time.ctime())

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print('\nstarting',self.name,'at:',time.ctime())
        self.result = self.func(*self.args)
        print('\n',self.name,'finished at:',time.ctime())

    def getresult(self):
        return self.result
def main():
    threads = []
    for i in range(len(loops)):
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for i in range(len(loops)):threads[i].start()
    for i in range(len(loops)):threads[i].join()
    print('All done at:',time.ctime())

if __name__=='__main__':
    main()
