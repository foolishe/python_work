class StrKeyDict(dict):
    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key] # :把查找工作委托给__getitem__>>__missing__
        except KeyError:
            return default

    def __contains__(self,key):
        return key in self.keys() \
        or str(key) in self.keys()

test = StrKeyDict([('1','one'),('2','two'),('5','five')])

print(test[1],test['1'])
print(test.get(1))
print(1 in test,4 in test)

'''
“下面来看看为什么 isinstance(key, str) 测试在上面的 __missing__ 中是必需的。
如果没有这个测试，只要 str(k) 返回的是一个存在的键，
那么 __missing__ 方法是没问题的，不管是字符串键还是非字符串键，
它都能正常运行。但是如果 str(k) 不是一个存在的键，代码就会陷入无限递归。这是因为”
“__missing__ 的最后一行中的 self[str(key)] 会调用 __getitem__
，而这个 str(key) 又不存在，于是 __missing__ 又会被调用。”

摘录来自: [巴西] Luciano Ramalho. “流畅的Python。” Apple Books.
'''
import collections

ct = collections.Counter('fjjfklhugkjghduk')
ct.update('aafdjfslfjsl;')
print(ct.most_common(5))

print(ct)
