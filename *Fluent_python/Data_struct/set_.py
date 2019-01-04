import dis


dis.dis('{1}')

dis.dis('set([1])')

print(frozenset(range(10)))

from unicodedata import name

s={chr(i) for i in range(32,256) if
    'SIGN' in name(chr(i),'')}
print(name(chr(50),''))
print(s)
