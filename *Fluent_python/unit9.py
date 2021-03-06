from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x,self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
            bytes(array(self.typecode,self)))

    def __eq__(self,other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    @classmethod
    def frombytes(*args):
        typecode = chr(args[1][0])
        memv = memoryview(args[1][1:]).cast(typecode)
        print(locals())
        return args[0](*memv)

    def __format__(self,fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self),self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({},{})'
        components = (format(c,fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y,self.x)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Shortvector2d(Vector2d):
    typecode = 'f'

sv = Shortvector2d(1/11,1/28)
v = Vector2d(1/11,1/28)


#Test
print(len(bytes(v)))
print(len(bytes(sv)))
v1 = Vector2d(3,4)
print(v1.x,v1.y)
x,y = v1
print(x,y)
print(repr(v1))
v1_clone = eval(repr(v1))
print (v1 ==v1_clone)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1),bool(Vector2d(0,0)))
v1_clone = sv.frombytes(bytes(v1))
print(repr(v1_clone))
print(format(v1))
print(format(Vector2d(1,1),'p'))
print(format(Vector2d(1,1),'.3ep'))
print(format(Vector2d(1,1),'0.5fp'))
