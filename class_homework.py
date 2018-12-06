#餐馆对象模型，客户登录互动模型
import time
class restaurant():
    #number_guest=0 #创建类时调用函数时只会执行函数内的代码，所以不会重新赋值
    def __init__(self,name,type,number_served=0):
        self.name=name
        self.type=type
        self.number_served=number_served
        self.number_guest+=1
    number_guest=0
    def set_number_served(self):#函数名不要与变量名冲突，不然会有意想不到的的错误。
        print(f'\n{self.number_served} Guest!\nHad Be Served.')

    def describe_restaurant(self):
        print(f'hello,everyone.welcome come in {self.name},this is a {self.type} restaurant ')

    def open_restaurant(self):
        print(time.ctime())
        print('The restaurant open time is 7:00--24:00 everyday!welcome')

    def increment_number_served(self,max_number_guest):
        left_guest_serveable=max_number_guest-self.number_guest
        print(f'Today!The restaurant already Served {self.number_guest} '+
        f'guest.almost can be recive {left_guest_serveable} Guest more')


eat=restaurant('ABT','fastfood')
kendeji=restaurant('KFC','fasteating')
eat.describe_restaurant()
eat.open_restaurant()
eat.set_number_served()
eat.increment_number_served(50)
kendeji.describe_restaurant()
kendeji.open_restaurant()
kendeji.set_number_served()
kendeji.increment_number_served(50)


class user():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0

    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f'u alreay login {self.login_attempts} times')

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f'u alreay login {self.login_attempts} times')

    def discribe_user(self):
        print(f'user name: {self.first_name.title()} {self.last_name.title()}')

    def greet_user(self):
        print(f'hello,{self.first_name.title()} {self.last_name.title()},welcome back.')

alex=user('alex','jinear')
jineari=user('eairl','jan')
alex.discribe_user()
alex.greet_user()
for i in range(10):
    alex.increment_login_attempts()
alex.reset_login_attempts()
jineari.discribe_user()
jineari.greet_user()
i=0
while i <10:
    jineari.increment_login_attempts()
    i=i+1
jineari.reset_login_attempts()
