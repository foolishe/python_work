import collections,random

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit)
            for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]



print(Card('7','diamonds'))
deck = FrenchDeck()
print(deck[5])
print(random.choice(deck))
# __getitem__:切片,迭代
print(deck[:3])
print(deck[12: :13])#11-2+4
for card in deck[0:6]:
    print(card)
for card in reversed(deck[0:6]):
    print(card)
print(Card('Q','hearts') in deck)
print(len(deck))#len('any class')

print('\n迭代>排序')
suit_values = dict(spades=3,hearts=1.1,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * 4 + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)

"""
“虽然 FrenchDeck 隐式地继承了 object 类，5 但功能却不是继承而来的。
 __len__ 和 __getitem__ 这两个特殊方法，
 FrenchDeck 就跟一个 Python 自有的序列数据类型一样，
 可以体现出 Python 的核心语言特性（例如迭代和切片）。
 同时这个类还可以用于标准库中诸如
 random.choice、reversed 和 sorted 这些函数。
 另外，对合成的运用使得 __len__ 和 __getitem__ 的具体实现
 可以代理给 self._cards 这个 Python 列表（即 list 对象）。”

摘录来自: [巴西] Luciano Ramalho. “流畅的Python。” Apple Books.
"""
