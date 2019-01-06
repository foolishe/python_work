def factorial(n):
    if n < 2: return 1
    return n * factorial(n-1)

fac = factorial # fac = factorial() will be wrong.
print(fac,'\n',fac(3))

print(list(map(factorial,range(6))))
print([factorial(n) for n in range(6)])

print(list(map(fac,filter(lambda n: n % 2,range(6)))))
print([fac(i) for i in range(6) if i % 2])

from functools import reduce
from operator import add

print(reduce(add,range(100)),
    sum(range(100)))

def tag(name,*content,cls=None,**attrs):
    #生成html标签,cls:class
    'tag函数签名中没有明确指定名称的关键字参数会被**attrs捕获,并存入一个字典'
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ' '.join('%s="%s"' %(attr,value)
            for attr,value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>' %(name,attr_str,c,name)
            for c in content)
    else:
        return '<%s %s />' %(name,attr_str)

my_tag =dict([('name','img'),('title','Sunset Boulevard'),
    ('src','sunset.jpg'),('cls','framed')])
print(
    tag('br'),
    '\n',
    tag('p','hello','world'),'\n',
    tag('p','hello','world',cls='sidebar'),'\n',
    tag(content='testing',name='img'),'\n',
    #tag(content='testing','img','\n'),
    tag(**my_tag),

)

'装饰器'
'''
    import bobo

    @bobo.query('/')
    def hello(person):
        return 'Hello %s!' % person

    “bobo.query 装饰器把一个普通的函数（如 hello ）与框架的请求处理机制集成起来了。
    装饰器会在第 7 章讨论，这不是这个示例的关键。这里的关键是，
    Bobo 会内省 hello 函数，发现它需要一个名为 person 的参数，
    然后从请求中获取那个名称对应的参数，将其传给 hello 函数，
    因此程序员根本不用触碰请求对象。”

摘录来自: [巴西] Luciano Ramalho. “流畅的Python。” Apple Books.
'''

from operator import mul
from functools import partial

triple = partial(mul,3)
print(
triple(8),
'\n',
list(map(triple,range(1,10)))
)
