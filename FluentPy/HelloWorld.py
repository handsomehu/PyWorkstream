import collections
from math import hypot
import builtins
import time
from vector2d import Vector2d

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)

    return rank_value * len(suit_values) + suit_values[card.suit]




beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
    print(card)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
            for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value): #
        self._cards[position] = value

    def __delitem__(self, position): #
        del self._cards[position]

    def insert(self, position, value): #
        self._cards.insert(position, value)


def deco(function):
    def inner():
        print("running inner!")
    return inner

@deco
def target():
    print("running target!")

target()

v1 = Vector2d(3,4)
print(abs(v1))
print(hash(v1))


def simple_coroutine(): #
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)




def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
print(coro_avg.send(5))

my_coro = simple_coroutine()
print(my_coro)
next(my_coro)
time.sleep(3)
my_coro.send(18)