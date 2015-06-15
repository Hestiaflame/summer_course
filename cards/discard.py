# discard.py
# -------
# by Hestiaflame

from card import Card
from random import shuffle

class Discard_pile():
    	"A discard pile"


# This saves the attributes of deck for later.
    	def __init__(self):
		self.cards = []

# This shows what the class is as specifically as possible. Not meant to be turned into a string.
	def __repr__(self):
		return "<discard pile with {} cards>".format(self.count())

# Shuffle pile
	def mix(self):
		shuffle(self.cards)

# Count the number of cards in the deck
	def count(self):
		return len(self.cards)

# Add a card
	def add(self, card):
		self.cards.append(card)
