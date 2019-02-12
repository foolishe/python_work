“import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  ➊
        offset = position * '  |'  ➋
        print(ROW_FMT.format(needle, position, offset))  ➌

if __name__ == '__main__':

    if sys.argv[-1] == 'left':  ➍
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  ➎
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


“>>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
...     i = bisect.bisect(breakpoints, score)
...     return grades[i]
...
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
❶ 用特定的 bisect 函数来计算元素应该出现的位置。
“
import bisect
import random

SIZE=7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“>>> from array import array  ➊
>>> from random import random
>>> floats = array('d', (random() for i in range(10**7)))  ➋
>>> floats[-1]  ➌
0.07802343889111107
>>> fp = open('floats.bin', 'wb')
>>> floats.tofile(fp)  ➍
>>> fp.close()
>>> floats2 = array('d')  ➎
>>> fp = open('floats.bin', 'rb')
>>> floats2.fromfile(fp, 10**7)  ➏
>>> fp.close()
>>> floats2[-1]  ➐
0.07802343889111107
>>> floats2 == floats  ➑
True
”
“>>> numbers = array.array('h', [-2, -1, 0, 1, 2])
>>> memv = memoryview(numbers)  ➊
>>> len(memv)
5
>>> memv[0]  ➋
-2
>>> memv_oct = memv.cast('B')  ➌
>>> memv_oct.tolist()  ➍
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
>>> memv_oct[5] = 4  ➎
>>> numbers”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“
>>> import numpy  ➊
>>> a = numpy.arange(12)  ➋
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10,  11])
>>> type(a)
<class 'numpy.ndarray'>
>>> a.shape  ➌
(12,)
>>> a.shape = 3, 4  ➍
>>> a
array([[  0,  1,  2,  3],
       [  4,  5,  6,  7],
       [  8,  9, 10, 11]])
>>> a[2]  ➎
array([  8,  9,  10,  11])
>>> a[2, 1]  ➏
9
>>> a[:, 1]  ➐
array([1, 5, 9])
>>> a.transpose() ➑
array([[  0,  4,  8],
       [  1,  5,  9],
       [  2,  6, 10],
       [  3,  7, 11]])
❶ 安装 NumPy 之后，导入它（NumPy 并不是 Python 标准库的一部分）。

❷ 新建一个 0~11 的整数的 numpy.ndarry ，然后把”
“>>> from collections import deque
>>> dq = deque(range(10), maxlen=10)  ➊
>>> dq
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
>>> dq.rotate(3)  ➋
>>> dq
deque([7, 8, 9, 0, ”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
>>> dq.rotate(-4)
>>> dq
deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
>>> dq.appendleft(-1)  ➌
>>> dq
deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
>>> dq.extend([11, 22, 33])  ➍
>>> dq
deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
>>> dq.extendleft([10, 20, 30, 40])  ➎
>>> dq
deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“mport sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            occurrences = index.get(word, [])  ➊
            occurrences.append(location)       ➋
            index[word] = occurrences          ➌
            # 以字母顺序打印出结果
for word in sorted(index, key=str.upper):      ➍
    print(word, index[word])”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“class StrKeyDict0(dict):  ➊

    def __missing__(self, key):
        if isinstance(key, str):  ➋
            raise KeyError(key)
        return self[str(key)]  ➌

    def get(self, key, default=None):
        try:
            return self[key]  ➍
    except KeyError:
        return default  ➎

def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()  ➏
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“class StrKeyDict0(dict):  ➊

    def __missing__(self, key):
        if isinstance(key, str):  ➋
            raise KeyError(key)
        return self[str(key)]  ➌

    def get(self, key, default=None):
        try:
            return self[key]  ➍
    except KeyError:
        return default  ➎

def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()  ➏
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“from types import MappingProxyType
>>> d = {1:'A'}
>>> d_proxy = MappingProxyType(d)
>>> d_proxy
mappingproxy({1: 'A'})
>>> d_proxy[1]  ➊
'A'
>>> d_proxy[2] = 'x'  ➋
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'mappingproxy' object does not support item assignment
>>> d[2] = 'B'
>>> d_proxy  ➌
mappingproxy({1: 'A', 2: 'B'})
>>> d_proxy[2]
'B”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books. 
Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
❷利用该位置来算出需要几个分隔符号。

❸ 把元素和其应该出现的位置打印出来。

❹ 根据命令上最后一个参数来选用 bisect 函数。

❺ 把选定的函数在抬头打印出来。

”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
