from random import shuffle

class Deck:
  def __init__(self) -> None:
      self.cards = []
      for i in range(2,14):
        for j in range(4):
            self.cards.append(self.card(i,j))
        shuffle(self.cards)

  def rm_card(self):
    if len (self.cards) ==0:
      return
    return self.cards.pop
          