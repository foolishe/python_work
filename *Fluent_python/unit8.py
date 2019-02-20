import weakref

class Cheese:

    def __init__(self,kind):
        self.kind = kind

    def __repr__(self):
        return f'Cheese({self.kind})'


stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilstit'),Cheese('Brie'),
    Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
print(list(stock.values()))

del catalog
print(sorted(stock.keys()))

del cheese

print(sorted(stock.keys()))
