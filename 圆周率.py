from time import perf_counter
from random import random
star=perf_counter()
numb=pow(2,19)
hit=0.0
for i in range(1,numb+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1:
        hit+=1
a=4*hit/numb
print('圆周率：{}  程序运行时间t={:.5f}s'.format(a,perf_counter()-star))
        

