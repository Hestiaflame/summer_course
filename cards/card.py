# card.py
# -------
# by Hestiaflame

from card import Card
from random import shuffle

class Deck():
    	"A deck represents a normal deck with 52 cards"


# This saves the attributes of deck for later.
    	def __init__(self):
		self.cards = [Card(card_num) for card_num in range(52)]

# This shows what the class is as specifically as possible. Not meant to be turned into a string.
	def __repr__(self):
		return "<Deck with {} cards>".format(self.num_cards)

# Shuffle deck
	def mix(self):
		shuffle(self.cards)

# Draw a card
	def draw(self):
		if count() == 0:
			return None
		else:
			return self.cards.pop()

# Look at top card
	def peek(self):
		return self.cards[len(self.cards) - 1]

# Count the number of cards in the deck
	def count(self):
		return len(self.cards)

# Check if the deck is empty
	def empty(self):
		if count() == 0:
			return True
		else:
			return False

# Add a card
	def add(self, card):
		self.cards.append(card)

