from concurrent import futures
from time import sleep,strftime

def display(*args):
    print(strftime('[%H:%M:%S]'),end= ' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}):doing nothing for {}s...'
    display(msg.format('\t'*n,n,n))
    sleep(n)
    msg = '{}loiter({}):done.'
    display(msg.format('\t'*n,n))
    return n * 10

def main():
    display('Script staring.')
    executor = futures.ThreadPoolExecutor(max_workers=5)
    results = executor.map(loiter,[6,3,4,5,4])
    display('\nresult:',results)
    display('Waiting for individual results:')
    for i ,result in enumerate(results):
        display('result{}: {}'.format(i,result))

main()
