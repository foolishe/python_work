import collections,random

Card = collections.namedtuple('Card',['rank','suit'])


class FrenchDeck(collections.MutableSequence):
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

    def __setitem__(deck,position,card):
        deck._cards[position] = card

    def __getitem__(self,position):
        return self._cards[position]

    def inset(self,position,value):
        self._cards.insert(position,value)

'''
    try:
        field_names = field_names.replace(',',' ').split()
    except AttributeError:
        pass
    field_names = tuple(field_names)

'''

import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self,iterable):
        'iter element from list'

    @abc.abstractmethod
    def pick(self):
        'randomize pop some element,if object is empty raise LookupError'

    def loaded(self):
        'if have any element return True,else return False'
        return bool(self.inspect())

    def inspect(self):
        'return a sorted tuple of object\'s current element '
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):

    def __init__(self,items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self,items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()



class Lotteryblower(Tombola):

    def __init__(self,iterable):
        self._balls = list(iterable)

    def load(self,iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except valueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls[position]

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))



class Sized(metaclass = abc.ABCMeta):
    __slots__ = ()

    @abc.abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls,c):
        if cls is Sized:
            if any('__len__' in b.__dict__ for b in c.__mro__):
                return True
        return NotImplemented

print(Tombola._abc_registry_clear())
import dis

print(dis.dis(Tombola))
