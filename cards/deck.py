# card.py
# -------
# by Maya Malavasi

# This defines a playing card. The card is defined by an int. For example, 0 is the 2 of Clubs, 51 is
# the Ace of Spades
from card import Card
from random import shuffle

class Deck():
    	"A deck represents a normal deck with 52 cards"


# This saves the attributes of card for later.
    	def __init__(self):
		self.cards = [Card(card_num) for card_num in range(52)]
		self.discard_pile = []
		self.num_cards = 52

# This shows what the class is as specifically as possible. Not meant to be turned into a string.
	def __repr__(self):
		return "<Deck with {} cards>".format(self.num_cards)

	def mix(self):
		shuffle(self.cards)

	def draw(self):
		if self.num_cards == 0:
			return None
		else:
			last_card = self.cards.pop()
			self.discard_pile.append(last_card)
			return last_card

	def peek(self):
		return self.cards[len(self.cards) - 1]

	def count(self):
		return len(self.cards)

	def empty(self):
		if self.num_cards == 0:
			return True
		else:
			return False

	def add(self, card):
		self.cards.append(card)

	def finish(self):
		for each_card in self.cards:
			self.discard_pile.append(each_card)
		self.cards = []
		self.num_cards = 0

	def refill(self):
		for each_card in self.discard_pile:
			self.cards.append(each_card)
		self.discard_pile = []
		self.num_cards = 52

