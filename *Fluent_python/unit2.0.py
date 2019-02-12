import bisect
import sys

HAYSTACK = [1,4,5,6,9,8,8,12,16,15,30,20,24,24,34,23]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK,needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle,position,offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        print(1)
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:',bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in sorted(HAYSTACK)))
    demo(bisect_fn)




def grade(score,breakpoint=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoint,score)
    return grades[i]


for i in (grade(score) for score in [33,99,77,70,90,100]):
    'stupid code , just try it !'
    print(i,end=' ')




import random

SIZE = 7
random.seed(1729)
my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list,new_item)
    print(my_list)
