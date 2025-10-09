import collections

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
    # By implementing the __getitem__ method, the deck is
    # also iterable
    return self._cards[position]

if __name__ == '__main__':
  deck = FrenchDeck()
  assert len(deck) == 52
  assert deck[:3] == [
    Card(rank='2', suit='spades'),
    Card(rank='3', suit='spades'),
    Card(rank='4', suit='spades')
  ]

  #for card in reversed(deck):
  #  print(card)

  assert True == Card('Q', 'hearts') in deck
  assert False == Card('7', 'beasts') in deck
