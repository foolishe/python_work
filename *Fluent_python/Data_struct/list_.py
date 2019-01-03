symbols = ')%Ykl#'

codes = [ord(symbol)
 for symbol
 in symbols]

print(codes)

beyond_ascii = [ord(s) for s in symbols
    if ord(s)>50]
print(beyond_ascii)
beyond_asci = list(filter(lambda c:c>67,map(ord,symbols)))
print(beyond_asci)

colors = ['black','white']
sizes = ['s','m','l']
tshirts = [(colors,size)
    for colors in colors
    for size in sizes]

print(tshirts)

print(tuple(ord(symbol) for symbol in symbols))

import array

print(array.array('I',(ord(symbol) for symbol in symbols)))

for tshirt in ('%s : %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)
