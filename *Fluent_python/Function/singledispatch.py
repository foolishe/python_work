import html
from functools import singledispatch
from collections import abc
import numbers

@singledispatch
def htmlize(obj):
        content = html.escape(repr(obj))
        return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n','<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
@htmlize.register(abc.MutableSet)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item)
    for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

print(htmlize({2,3,4}),'\n',
htmlize('abs'),'\n',
htmlize(54),'\n',
htmlize(['alpha',66,{5,4,3},])
)
# .format(**local()),用户可以控制输出.
