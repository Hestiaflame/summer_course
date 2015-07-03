# deck.py
# -------
# by Hestiaflame

from card import Card
from random import shuffle
#from random import seed


class Deck():
    	"A deck represents a normal deck"


# This saves the attributes of deck for later.
    	def __init__(self, cards=None, shuffle=False):
		if cards == None:
			self.cards = []
		else:
			self.cards = [Card(card_num) for card_num in cards]
		if shuffle == True:
			self.mix()

# This shows what the class is as specifically as possible. Not meant to be turned into a string.
	def __repr__(self):
		return "<Deck with {} cards: {}>".format(self.count(), self.cards)

# Shuffle deck
	def mix(self):
		shuffle(self.cards)

# Count the number of cards in the deck
	def count(self):
		return len(self.cards)

# Draw a card
	def draw(self):
		if self.count() == 0:
			return None
		else:
			return self.cards.pop()

# Look at top card
	def peek(self):
		return self.cards[len(self.cards) - 1]


# Check if the deck is empty
	def empty(self):
		if self.count() == 0:
			return True
		else:
			return False

# Add a card
	def add(self, card):
		self.cards.append(card)

	def add_deck(self, deck):
		while len(deck.cards) > 0:
			self.cards.append(deck.cards.pop(0))

