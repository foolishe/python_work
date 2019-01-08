# 函数重构策略模式,最佳折扣实现.

from collections import namedtuple

Customer = namedtuple('Customer','name fidelity')

class LineItem:
    def __init__(self,product,quantity,price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:

    def __init__(self,customer,cart,promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self,'__total'):
            self.__total = sum(item.total()
                for item in self.cart)
            return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:  {:.2f} due: {:.2f}'
        return fmt.format(self.total(),self.due())

def fidelity_promo(order):
    return order.total() * .5 if\
    order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
        return diacount

def large_order_promo(order):
    distinct_items = {item.product for item in
        order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
print(globals())
#promos = [fidelity_promo,bulk_item_promo,large_order_promo]
promos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']
'动态收集折扣策略'

def best_promo(order):
    return max(promo(order) for promo in promos)


'''“globals()

　返回一个字典，表示当前的全局符号表。这个符号表始终针对当前模块
（ 对函数或方法来说，是指定义它们的模块，而不是调用它们的模块）。”


“对接口编程，而不是对实现编程”和“优先使用对象组合，而不是类继承”。”

摘录来自: [巴西] Luciano Ramalho. “流畅的Python。” Apple Books.

'''
