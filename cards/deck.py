# deck.py
# -------
# by Hestiaflame

from card import Card
from random import shuffle

class Deck():
    	"A deck represents a normal deck with 52 cards"


# This saves the attributes of deck for later.
    	def __init__(self):
		self.cards = [Card(card_num) for card_num in range(52)]
		self.discard_pile = []
		self.num_cards = 52

# This shows what the class is as specifically as possible. Not meant to be turned into a string.
	def __repr__(self):
		return "<Deck with {} cards>".format(self.num_cards)
# Shuffles the deck
	def mix(self):
		shuffle(self.cards)

# Draws a card
	def draw(self):
		if self.num_cards == 0:
			return None
		else:
			last_card = self.cards.pop()
			self.discard_pile.append(last_card)
			self.num_cards -= 1
			return last_card

# Shows the top card in the deck
	def peek(self):
		return self.cards[len(self.cards) - 1]

# Tells you how many cards are in the deck
	def count(self):
# len(self.cards) should equal num_cards - you can replace it if you would like.
		return len(self.cards)

# Checks if the deck is empty
	def empty(self):
		if self.num_cards == 0:
			return True
		else:
			return False

# Adds a card
	def add(self, card):
		self.cards.append(card)
		self.num_cards += 1

# Empties the deck
	def finish(self):
		for each_card in self.cards:
			self.discard_pile.append(each_card)
		self.cards = []
		self.num_cards = 0

# Refills the deck
	def refill(self):
		for each_card in self.discard_pile:
			self.cards.append(each_card)
		self.discard_pile = []
		self.num_cards = 52

