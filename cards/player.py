# player.py
# -------
# by Hestiaflame

from card import Card
from deck import Deck
from random import shuffle
from random import randint



# player for Crazy Eights

class CrazyEightsPlayer():

# This saves the attributes of deck for later.
    	def __init__(self, cards):
		self.cards = cards

# This shows what the class is as specifically as possible. Not meant to be turned into a string.
	def __repr__(self):
		return "<Hand with {} cards>".format(self.count())


# Count the number of cards in the hand
	def count(self):
		return len(self.cards)


# Check if the deck is empty
	def empty(self):
		if len(self.cards) == 0:
			return True
		else:
			return False


# Shorter way to do that.
#	def empty(self):
#		return len(self.cards) == 0:
# But I don't fully understand it yet.




# Add a card
	def add(self, card):
		self.cards.append(card)

# Play a card
	def get_play(self, prev_card):
		if not self.empty():
			for each_card in self.cards:
				if each_card.suit() == prev_card.suit() and each_card.rank() != "8":
					index_return = self.cards.index(each_card)
					return self.cards.pop(index_return)
				elif  each_card.rank() == prev_card.rank() and each_card.rank() != "8":
					index_return = self.cards.index(each_card)
					return self.cards.pop(index_return)
				
			for each_card in self.cards:
				if each_card.rank() == "8":
					print("------------------EIGHT------------------")
					eight = self.cards.pop(self.cards.index(each_card))
					new_eight = self.change_eight(eight)
					return new_eight
			self.draw_card()
			return prev_card


	def draw_card(self):
		card = self.game.draw()
		self.cards.append(card)

	def change_eight(self, eight):
		suit = randint(0, 3)
		eight.card_number = suit + 24
		return eight


#______________________________________________________________________________________________________











# player for War


class WarPlayer(Deck):
	"""Represents a player in a card game. When the player
	draws cards, she will draw from her draw deck. When the draw deck runs
	out, the discard pile will be shuffled into the draw deck. 
	When the player takes cards, they will go into the discard deck."""

	def __init__(self):
		"""Sets up the player's draw deck and discard deck. """
		self.cards = Deck()
		self.discardPile = Deck()

	def has_any_cards(self):
		"""returns True if the player has any cards in either the draw or 
		the discard deck. Otherwise returns False."""
		if self.cards.empty() and self.discardPile.empty():
			return False
		else:
			return True

	def take_card(self, card):
		self.cards.add(card)

	def take_deck(self, deck):
		"Adds the deck to the discard pile"
		self.discardPile.add_deck(deck)

	def draw_card(self):
		"""Draws (and returns) a card from the draw pile if possible. If not, 
		shuffles the discard pile into the draw pile. If there are still no
		cards, returns None."""
		if self.has_any_cards():
			if self.cards.empty():
				self.shuffle_discard_deck_into_draw_deck()
			return self.cards.draw()
		else:
			return None

	def shuffle_discard_deck_into_draw_deck(self):
		"""Adds the discard deck to the draw deck and then shuffles the draw
		deck. No return value"""
		self.cards.add_deck(self.discardPile)

