"""Deck Of Cards
Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

The Deck class should have a deal method to pop a single card from the deck.
After a card is dealt, it is removed from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K). """


from random import shuffle

class Card:
    # Write Code here
    def __init__(self, suit, value):
      self.suit = suit
      self.value = value

    def __repr__(self):
      return f"{self.value} of {self.suit}"

class Deck(Card):
  def __init__(self):
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    self.cards = [Card(i,j) for i in suits for j in values]    

  def deal(self):
    #to pop a single card from deck
    return self.cards.pop()


  def shuffle(self):
    #to shuffle the 52 cards
    if len(self.cards) < 52:
      print("Requirement - 52 cards")
    shuffle(self.cards)
     




    
game = Deck()
game.shuffle()
game.deal()
