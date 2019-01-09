def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count,total
        count+=1
        total += new_value
        return total / count
    return averager

avg = make_averager()
#print(avg(10),avg(11))

import time,functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0 = time.time()
        result = func(*args,**kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k, w in
                sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs) %s(%s) -> %s]' %
            (elapsed,name,arg_str,result))
        return result
    return(clocked)

@functools.lru_cache()#least recently used cache
@clock
def fibonacci(n):
    if n<2:return n
    return fibonacci(n-2) + fibonacci(n-1)
if __name__=='__main__':
    print(fibonacci())
