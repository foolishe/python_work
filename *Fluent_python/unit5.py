# about () >> __call__ >>callable

import random

class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

# function specil method

def tag(name,*content,cls=None,**attrs):
    #关键字参数和仅限关键字参数
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s" ' %(attr,value)
            for attr,value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>' %(name,attr_str,c,name)
            for c in content)
    else:
        return '<%s %s />' %(name,attr_str)


#
def clip(text,max_len=80):
     end = None
     if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        if space_before >= 0:
             end = space_before
        else:
            space_after = text.rfind(' ',max_len)
        if space_after >= 0:
            end = space_after
     if end == None:
        end = len(text)
     return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)


from inspect import signature

sig = signature(clip)
print(
 ''
)
print(sig)

for name,param in sig.parameters.items():
    print(param.kind,':',name,'=',param.default)


sig = signature(tag)
my_tag = {'name':'img','title':'Sunset Boulevard',
    'src':'sunset.jpg','cls': 'framed'}
bound_args = sig.bind(**my_tag)

print(bound_args)
del my_tag['name']
print(bound_args)
# bound_args = sig.bind(**my_tag)
print(bound_args)



from operator import methodcaller

s = 'The time has come'

upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace',' ','-')
print(hiphenate(s))

print(hiphenate)

from functools import partial

picture = partial(tag, 'img', cls='pic-frame')
print(picture)
print(picture(src='wumpus.jpeg'))
print(picture.args,picture.keywords)
