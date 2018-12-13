from class_homework import restaurant,user
class IceCreamStand(restaurant):
    def __init__(self,name,type,*flavors_icecreamstands): #添加新参数
        super().__init__(name,type,number_served=0)#继承父类的方法。
        self.flavors_icecreamstands=flavors_icecreamstands

    def show_flavors_icecreamstands(self):
        print('flavors icecream is:\t ')
        for flavors_icecreamstand in self.flavors_icecreamstands[0]:
            print(flavors_icecreamstand+' ' ,end='')
        print('\n')
if __name__=='__main__':
    flavors=['cofe','apple','orange']
    rich=IceCreamStand('relax','IceCreamStand',flavors)
    rich.show_flavors_icecreamstands()
    rich.describe_restaurant()
    rich.increment_number_served(20)

class Admin(user):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=privilege()#添加类为子属性
    #def show_privileges(self):
        #print(f'Admin\'s privileges: ')
        #for privilege in self.privileges:
            #print('\t'+privilege)
class privilege():
    #privileges=['can add post','can delete post','can ban user']
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):#一定记得加self
        print(f'Admin\'s privileges: ')
        for privilege in self.privileges:
            print('\t'+privilege)
    def add_admin_privileges(self,new):
        self.privileges.append(new)
if __name__=='__main__':
    hello=Admin('jin','earl')
    hello.privileges.show_privileges()
    hello.discribe_user()
    hello.greet_user()
    hello.increment_login_attempts()
    hello.increment_login_attempts()
    hello.privileges.add_admin_privileges('happy')
    hello.privileges.show_privileges()
    hiya=Admin('love','kiki')
    hiya.greet_user()
    hiya.privileges.show_privileges()
