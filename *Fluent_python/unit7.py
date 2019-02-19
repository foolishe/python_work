import time
from collections import Counter
from functools import lru_cache
import functools


counter = Counter()

def clock(func):
    #@functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__+str(args)
        counter[name] = counter.get(name,0) + 1
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed,name,arg_str,result))
        return result
    return clocked


def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

factorial = clock(factorial)


factorial(9)

@clock
@lru_cache(maxsize=1024)
def feb(n):
    return n if n<2 else feb(n-2)+feb(n-1)

feb(9)
print(counter,
'\n',feb)


def clock(func):
    def clocked(*args,**kwargs):
        t0 = time.time()
        result = func(*args,**kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' %(elapsed,name,arg_lst,result))
        return result
    return clocked


from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n','<br>\n')
    return f'<p>{content}</p>'

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(self):
    inner = '</li>\n<li>'.join(htmlize(item) for item in self)
    return  '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize(['hello',21,['i love u']]))


registry = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)-.decorate(%s)' % (active,func))
        if active:
            register.add(func)
        else:
            register.discard(func)
    return decorate



DEFAULT_FMT = '[{elapsed:0.8f}s] {name} ({args}) -> {result}'
def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            print(locals())
            return result
        return clocked
    return decorate


@clock() #
def f(n):
    return 1 if n<2 else f(n-1)+f(n-2)

f(8)
