
"""
>>> from unit10 import Vector

>>> Vector(range(10))
Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

>>> format(Vector([-1,-1,-1,-1]),'h')
'<2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>'
>>> v1 = Vector([3,4])
>>> v1
Vector([3.0, 4.0])
>>> octets = bytes(v1)
>>> octets
b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
>>> abs(v1)
5.0
>>> bool(v1),bool(Vector([0,0]))
(True, False)
>>> v1_clone = Vector.frombytes(bytes(v1))
>>> v1_clone
Vector([3.0, 4.0])
>>> v1 == v1_clone
True
>>> v1 == eval(repr(v1))
True
>>> v2 = Vector(range(7))
>>> v2
Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
>>> abs(v2) # doctest:+ELLIPSIS
9.53939201...

>>> len(v2)
7

>>> v2[0], v2[len(v2)-1], v2[-1],v2[1:5]
(0.0, 6.0, 6.0, Vector([1.0, 2.0, 3.0, 4.0]))

>>> v2.x
0.0
>>> v2.x = 4
>>> v2.x
4
>>> v2.z
2.0
>>> hash(v2)
3
>>> v2.z = 4.444

>>> hash(v2)


"""


if __name__ == '__main__':

    import doctest

    doctest.testmod()
