“>>> import weakref
>>> stock = weakref.WeakValueDictionary()  ➊
>>> catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
...                 Cheese('Brie'), Cheese('Parmesan')]
...
>>> for cheese in catalog:
...     stock[cheese.kind] = cheese  ➋
...
>>> sorted(stock.keys())
['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']  ➌
>>> del catalog
>>> sorted(stock.keys())
['Parmesan']  ➍
>>> del cheese
>>> sorted(stock.keys())
[]”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“from array import array
import reprlib
import math


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)  ➊

    def __iter__(self):
        return iter(self._components)  ➋

    def __repr__(self):
        components = reprlib.repr(self._components)  ➌
        components = components[components.find('['):-1]  ➍
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))  ➎

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))  ➏

    def __bool__(self):

        “def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]
        “def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)  ➊
        if isinstance(index, slice):  ➋
            return cls(self._components[index])  ➌
        elif isinstance(index, numbers.Integral):  ➍
            return self._components[index]  ➎
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))  ➏
”“shortcut_names = 'xyzt'

def __getattr__(self, name):
    cls = type(self)  ➊

    if len(name) == 1:  ➋
        pos = cls.shortcut_names.find(name)  ➌
        if 0 <= pos < len(self._components):  ➍
            return self._components[pos]
    msg = '{.__name__!r} object has no attribute {!r}'  ➎
    raise AttributeError(msg.format(cls, name))
“def __setattr__(self, name, value):
    cls = type(self)
    if len(name) == 1:  ➊
        if name in cls.shortcut_names:  ➋
            error = 'readonly attribute {attr_name!r}'
        elif name.islower():
            “      elif name.islower():  ➌
            error = "can't set attributes 'a' to 'z' in {cls_name!r}"
        else:
            error = ''  ➍
        if error:  ➎
            msg = error.format(cls_name=cls.__name__, attr_name=name)
            raise AttributeError(msg)
    super().__setattr__(name, value)
    “def __eq__(self, other):  # ➌
        return tuple(self) == tuple(other)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)  # ➍
        return functools.reduce(operator.xor, hashes, 0)
        “def __hash__(self):
    hashes = map(hash, self._components)
    return functools.reduce(operator.xor, hashes)

    “def __eq__(self, other):
    if len(self) != len(other):  # ➊
        return False
    for a, b in zip(self, other):  # ➋
        if a != b:  # ➌
            return False
    return True
    “def __eq__(self, other):
    return len(self) == len(other) and all(a == b for a, b in zip(self, other))
    “def angle(self, n):  ➋
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r,
        “a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):  ➌
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):  # 超球面坐标
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
                                     self.angles())  ➍
            outer_fmt = '<{}>'  ➎
        else:
            coords = self
            outer_fmt = '({})'  ➏
        components = (format(c, fmt_spec) for c in coords)  ➐
        return outer_fmt.format(', '.join(components))  ➑

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.  ”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books. ”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“from itertools import zip_longest  # ➍
>>> list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1))
[(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2), (-1, -1, 3.3)]”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“>>> format(Vector([-1, -1, -1, -1]), 'h')
'<2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>'
>>> format(Vector([2, 2, 2, 2]), '.3eh')
'<4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>'
>>> format(Vector([0, 1, 0, 0]), '0.5fh')
'<1.00000, 1.57080, 0.00000, 0.00000>'
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“"
A multidimensional ``Vector`` class, take 5

A ``Vector`` is built from an iterable of numbers::

    >>> Vector([3.1, 4.2])
    Vector([3.1, 4.2])
    >>> Vector((3, 4, 5))
    Vector([3.0, 4.0, 5.0])
    >>> Vector(range(10))
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    “Tests with two dimensions (same results as ``vector2d_v1.py``)::

    >>> v1 = Vector([3, 4])
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    >>> v1
    Vector([3.0, 4.0])
    >>> v1_clone = eval(repr(v1))
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0)
    >>> octets = bytes(v1)
    >>> octets
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
    >>> abs(v1)
    5.0
    >>> bool(v1), bool(Vector([0, 0]))
    (True, False)


Test of ``.frombytes()`` class method:

    >>> v1_clone = Vector.frombytes(bytes(v1))
    >>> v1_clone
    Vector([3.0, 4.0])
    >>> v1 == v1_clone
    True


Tests with three dimensions::

    >>> v1 = Vector([3, 4, 5])
    >>> x, y, z = v1
    >>> x, y, z
    (3.0, 4.0, 5.0)
    >>> v1
    Vector([3.0, 4.0, 5.0])
    >>> v1_clone = eval(repr(v1))
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0, 5.0)
    >>> abs(v1)  # doctest:+ELLIPSIS
    7.071067811...
    >>> bool(v1), bool(Vector([0, 0, 0]))
    (True, False)


Tests with many dimensions::

    >>> v7 = Vector(range(7))
    >>> v7
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    >>> abs(v7)  # doctest:+ELLIPSIS
    9.53939201...

Test of ``.__bytes__`` and ``.frombytes()`` methods::

    >>> v1 = Vector([3, 4, 5])
    >>> v1_clone = Vector.frombytes(bytes(v1))
    >>> v1_clone
    “>>> v1 = Vector([3, 4, 5])
    >>> v1_clone = Vector.frombytes(bytes(v1))
    >>> v1_clone
    Vector([3.0, 4.0, 5.0])
    >>> v1 == v1_clone
    True


Tests of sequence behavior::

    >>> v1 = Vector([3, 4, 5])
    >>> len(v1)
    3
    >>> v1[0], v1[len(v1)-1], v1[-1]
    (3.0, 5.0, 5.0)


Test of slicing::

    >>> v7 = Vector(range(7))
    >>> v7[-1]
    6.0
    >>> v7[1:4]
    Vector([1.0, 2.0, 3.0])
    >>> v7[-1:]
    Vector([6.0])
    >>> v7[1,2]
    Traceback (most recent call last):
      ...
    TypeError: Vector indices must be integers


Tests of dynamic attribute access::

    >>> v7 = Vector(range(10))
    >>> v7.x
    0.0
    >>> v7.y, v7.z, v7.t
    (1.0, 2.0, 3.0)

Dynamic attribute lookup failures::

    >>> v7.k
    Traceback (most recent call last):
      ...
    AttributeError: 'Vector' object has no attribute 'k'
    >>> v3 = Vector(range(3))
    >>> v3.t
    Traceback (most recent call last):
      ...
    AttributeError: 'Vector' object has no attribute 't'
    >>> v3.spam
    Traceback (most recent call last):
      ...
    AttributeError: 'Vector' object has no attribute 'spam'


Tests of hashing::

    >>> v1 = Vector([3, 4])
    >>> v2 = Vector([3.1, 4.2])
    >>> v3 = Vector([3, 4, 5])
    >>> v6 = Vector(range(6))”
    “>>> hash(v1), hash(v3), hash(v6)
    (7, 2, 1)


Most hash values of non-integers vary from a 32-bit to 64-bit CPython build::

    >>> import sys
    >>> hash(v2) == (384307168202284039 if sys.maxsize > 2**32 else 357915986)
    True


Tests of ``format()`` with Cartesian coordinates in 2D::

    >>> v1 = Vector([3, 4])
    >>> format(v1)
    '(3.0, 4.0)'
    >>> format(v1, '.2f')
    '(3.00, 4.00)'
    >>> format(v1, '.3e')
    '(3.000e+00, 4.000e+00)'


Tests of ``format()`` with Cartesian coordinates in 3D and 7D::

    >>> v3 = Vector([3, 4, 5])
    >>> format(v3)
    '(3.0, 4.0, 5.0)'
    >>> format(Vector(range(7)))
    '(0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)'


Tests of ``format()`` with spherical coordinates in 2D, 3D and 4D::

    >>> format(Vector([1, 1]), 'h')  # doctest:+ELLIPSIS
    '<1.414213..., 0.785398...>'
    >>> format(Vector([1, 1]), '.3eh')
    '<1.414e+00, 7.854e-01>'
    >>> format(Vector([1, 1]), '0.5fh')
    '<1.41421, 0.78540>'
    >>> format(Vector([1, 1, 1]), 'h')  # doctest:+ELLIPSIS
    '<1.73205..., 0.95531..., 0.78539...>'
    >>> format(Vector([2, 2, 2]), '.3eh')
    '<3.464e+00, 9.553e-01, 7.854e-01>'
    >>> format(Vector([0, 0, 0]), '0.5fh')
    '<0.00000, 0.00000, 0.00000>'
    >>> format(Vector([-1, -1, -1, -1]), 'h')  # doctest:+ELLIPSIS
    '<2.0, 2.09439..., 2.18627..., 3.92699...>'
    >>> format(Vector([2, 2, 2, 2]), '.3eh')
    '<4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>'
    >>> format(Vector([0, 1, 0, 0]), '0.5fh[…]”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
   ”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.

”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.  # ➍”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.  # ➎
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.  ➏

”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.  ➌
            error = "can't se”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“>>> v7 = Vector(range(7))
    >>> v7[-1] ➊
    6.0
    >>> v7[1:4] ➋
    Vector([1.0, 2.0, 3.0])
    >>> v7[-1:] ➌
    Vector([6.0])
    >>> v7[1,2] ➍
    Traceback (most recent call last):
      ...”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books. ”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
“import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
”

Excerpt From: [巴西] Luciano Ramalho. “流畅的Python.” Apple Books.
