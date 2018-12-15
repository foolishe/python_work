# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 04:34:58 2018

@author: dontworry
"""

from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime


tlds=('com','edu','net','org','gov')
for i in range(randrange(5,11)):
     dtint=randrange(5231321131)
     dtstr=ctime(dtint)
     llen=randrange(4,8)
     login=''.join(choice(lc) for j in range(llen))#''.join([choice(lc) for i in range (llen)])
     dlen=randrange(llen,13)
     dom=''.join(choice(lc) for j in range(dlen))
     print('%s::%s@%s.%s::%d-%d-%d' %(dtstr,login,dom,choice(tlds),dtint,llen,dlen ))
     