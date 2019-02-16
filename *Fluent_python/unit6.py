from abc import ABC , abstractmethod
from collections import namedtuple
from functools import partial


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
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,'_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(),self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self,order):
        pass



class FidelityPromo(Promotion):

    def discount(self,order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):

    def discount(self,order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

class LargeOrderPromo(Promotion):

    def discount(self,order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0

class best_promotion(Promotion):

    def discount(self,order):
        return max([globals()[name]().discount(order)
            for name in globals()
            if name.endswith('Promo')])




joe = Customer('John Doe',1000)
ann = Customer('Ann Smith',1100)
cart = [LineItem('banana',4,0.5),
    LineItem('apple',10,1.5),
    LineItem('watermellon',5,5.0)]
print(Order(joe,cart,LargeOrderPromo()))
print(Order(joe,cart,best_promotion()))
#每次生成订单都会创建一个新对象实现回调，开销很大，可以使用python的一等函数特性直接使用函数实现回调
print(Order(ann,cart,FidelityPromo()))


long_order = [LineItem(str(item_code),1,1.0)
    for item_code in range(10)]


a = partial(Order,joe,long_order)
print(a(best_promotion()),'\n',a(BulkItemPromo()))
