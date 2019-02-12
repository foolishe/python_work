from array import array
from random import random

floats = array('d',(random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()
print('\n',floats2[-1],'\n',floats == floats2)
 #print 会在每个输出之间自动留空格

numbers = array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(memv.tolist(),' ',memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4

print(memv_oct.tolist(),' ',numbers)
