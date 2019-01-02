from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x,self.y)

    def __str__(self):
        return 'Vextor(%s,%s)' % (self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self)) #bool(self.x or self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x * scalar,self.y *scalar)

v = Vector(1,2)
t = Vector(7,7)
print(t * 5)
print(5 * t)

''' RESTART: /Users/longsen/github/python_work/*Fluent_python/dunder_method/Vector_ex.py
>>> t
Vector(7,7)
>>> print(t)
Vextor(7,7)
>>> t + v
Vector(8,9)
>>> print(t + v)
Vextor(8,9)
>>> '''
