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
		return "<Crazy eights player with {} cards>".format(self.count())


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


#

"""Once upon a time... there was a very annoying bug that I just couldn't fix.
By printing five hundred different things in half a dozen different locations, I eventually found that
the problem with the wrong card was occurring when there were two cards with the same rank in one hand,
with the correct card placed after the card with the wrong suit. The program would go up until it saw
that right double, and then attempt to go and find it again, at which point it would bump into the
wrong double and, since they had the same rank, think that the wrong card was the card it was looking
for, and therefore play it. I got around this bug by making an index number of my own, making it start
at zero before each "for each_ in __list", and increment-ing it by one every time it went through the
loop. With that, I was able to have the index of a certain card without having the index tied to the
placement of that particular card (and rank) in the list. It just directly goes and pops whatever that
card is at that index. (The End - lovely story right? :-))"""

# Play a card
	def get_play(self, prev_card):
		if not self.empty():
			index_return = 0

			print("My prev_card is {}".format(prev_card))

			for each_card in self.cards:
				print("EACH_CARD: {},  INDEX: {}".format(each_card, index_return))
				if each_card.suit() == prev_card.suit() and each_card.rank() != "8":

#					print("SUIT MATCH, suit is {}, INDEX OF {}".format(each_card.suit(), index_return))

					return self.cards.pop(index_return)
				elif  each_card.rank() == prev_card.rank() and each_card.rank() != "8":

					print("RANK MATCH, rank is {}, INDEX OF {}".format(each_card.rank(), index_return))

					return self.cards.pop(index_return)
				index_return += 1
				
			index_return = 0
			for each_card in self.cards:
				if each_card.rank() == "8":
					print("EIGHT")
					eight = self.cards.pop(self.cards.index(each_card))
					new_eight = self.change_eight(eight)
					return new_eight
				index_return += 1
			self.draw_card()
			return prev_card

	def change_eight(self, eight):
		suit = randint(0, 3)
		eight.card_number = suit + 24
		return eight
#


	def draw_card(self):
		card = self.game.draw()
		self.cards.append(card)


#______________________________________________________________________________________________________











# player for War


class WarPlayer():
	"""Represents a player in a card game. When the player
	draws cards, she will draw from her draw deck. When the draw deck runs
	out, the discard pile will be shuffled into the draw deck. 
	When the player takes cards, they will go into the discard deck."""

	def __init__(self):
		"""Sets up the player's draw deck and discard deck. """
		self.drawPile = Deck()
		self.discardPile = Deck()

	def __repr__(self):
		return "<{} cards>".format(self.count())

	def has_any_cards(self):
		"""returns True if the player has any cards in either the draw or +
		the discard deck. Otherwise returns False."""
		if self.drawPile.empty() and self.discardPile.empty():
			return False
		else:
			return True

	def take_card(self, card):
		self.discardPile.add(card)

	def count(self):
		return self.drawPile.count()

	def take_deck(self, deck):
		"Adds the deck to the discard pile"
		self.discardPile.add_deck(deck)


	def draw_card(self):
		"""Draws (and returns) a card from the draw pile if possible. If not, 
		shuffles the discard pile into the draw pile. If there are still no
		cards, returns None."""
		if self.has_any_cards():
			if self.drawPile.empty():
				self.shuffle_discard_deck_into_draw_deck()
			return self.drawPile.draw()
		return None

	def shuffle_discard_deck_into_draw_deck(self):
		"""Adds the discard deck to the draw deck and then shuffles the draw
		deck. No return value"""
		self.drawPile.add_deck(self.discardPile)
		self.drawPile.mix()

