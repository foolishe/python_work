from math import hypot

class Vector:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' %(self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __mul__(self,arg):
        return Vector(self.x * arg,self.y * arg)
