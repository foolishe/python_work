# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 03:52:00 2018

@author: dontworry
"""

import time
class GetUser():
    def __init__(self,name):
        self.name=str(name)
        print(f'hello,{self.name},welcome')
        with open('guest.txt','w') as f_object:
            f_object.write(self.name)
        with open('guest_book.txt','a') as f_object:
            f_object.write(f'{self.name} guest here at {time.ctime()}')
    
    def store_reason_like_program(self,reason):
        with open(f'{self.name}.txt','w') as f_object:
            f_object.write(reason+'\n')
        with open('guest_book.txt','a') as f_object:
            f_object.write(f'{self.name} guest here at {time.ctime()}')
    def show_why_like_program(self):
        with open(f'{self.name}.txt') as f_object:
           print('this is the reason why i like program:'.title())
           for line in f_object:
               print(line.strip())
    def show_guest_log(self):
        print(f'the log of {self.name} : ')
        with open(f'guest_book.txt') as f_object:
            for reason in f_object:
                print(reason.strip())

if __name__=='__main__':
    user_name=input('please input you name: ')
    try0=[]
    try0.append(user_name)
    print(try0[0])
    with open('guest.txt') as f_object:
        user_names=[]
        for name in f_object:
            user_names.append(name)
        print(user_names)   
        if not user_name in user_names:
            try0[0]=GetUser(user_name[:])#失败了不能创建用户输入的类，会创建一个try0[0]的类
        else:
            print(f'welcome back!{user_name.title()}')
            try0[0]=eval(try0[0])
    while True:
        reason=input('ok,so why you like program: ')
        if reason=='':
            break
        try0[0].store_reason_like_program(reason)
    try0[0].show_guest_log()
    try0[0].show_why_like_program()
    
    please input you name: alex
#alex
#['hellodavidhellohello']
#hello,alex,welcome
#
#ok,so why you like program: 
#the log of alex : 
#hello guest here at Sat Dec  8 05:07:27 2018david guest here at Sat Dec  8 05:12:00 2018hello guest here at Sat Dec  8 05:13:16 2018hello guest here at Sat Dec  8 05:13:28 2018hello guest here at Sat Dec  8 05:13:38 2018alex guest here at Sat Dec  8 05:14:11 2018
#This Is The Reason Why I Like Program:
#i just like it
#i want a job
#
#alex
#Traceback (most recent call last):
#
#  File "<ipython-input-43-5a01120580b5>", line 1, in <module>
#    alex
#
#NameError: name 'alex' is not defined
#
#
#
#
#try0[0]
#Out[44]: <__main__.GetUser at 0x2a7636269e8>
#
#    
