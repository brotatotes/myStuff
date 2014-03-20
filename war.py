#The card game "War"

#The "Card" object:
class Card:
  value = 0
  name = ''
  suit = 0  #1=diamonds; 2=clubs; 3=hearts; 4=spades
  def description(self):
    print "value = " + str(self.value) + '\n' + "name = " + self.name + '\n' + "suit = " + str(self.suit)
  def setCard(self, newValue, newName, newSuit):
    self.value = newValue
    self.name = newName
    self.suit = newSuit

#A Deck of Cards:
class Deck:
  cards = []
  def newDeck():
    names = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    suit = 0
    value = 0
    while suit < 4:
      suit = suit + 1
      for everyName in names:
        cards.append(Card.__init__(value, everyName, suit))
    print "New deck of cards created: " + str(cards)
      
            
