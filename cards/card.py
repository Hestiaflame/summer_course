# card.py
# -------
# by Maya Malavasi

# This defines a playing card. The card is defined by an int. For example, 0 is the 2 of Clubs, 51 is
# the Ace of Spades

class Card():
    	"A card represents a playing card"
	
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    	ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    	short_suits = ["C", "D", "H", "S"]
    	short_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


# This the attributes of card for later.
    	def __init__(self, card_number):
		if card_number > 51:
			raise ValueError("Card number cannot be over 51")
		if card_number < 0:
			raise ValueError("Card number cannot be less than 0")
		else:
			self.card_number = card_number


# This shows what the class is as specifically as possible. Not meant to be turned into a string.
	def __repr__(self):
		return "<{}>".format(self.short_name())


# This shows the attributes of the class in an attractive way.
	def __str__(self):
		return "{} of {}".format(self.rank(), self.suit())


# This takes two arguments finds out which is bigger
# If this one is bigger, return positive int
# If they are equal, return 0
# If the other one is bigger, return negative int

	def __cmp__(self, other_card):
		if self.rank() > other_card.rank():
			return 1
		elif self.rank() < other_card.rank():
			return -1
		else:
			return 0


	def rank(self):
		return self.ranks[self.card_number / 4]

	def suit(self):
		return self.suits[self.card_number % 4]

	def short_rank(self):
		return self.short_ranks[self.card_number / 4]

	def short_suit(self):
		return self.short_suits[self.card_number % 4]

	def name(self):
		return "{} of {}".format(self.rank(), self.suit())

	def short_name(self):
		return "{}{}".format(self.short_rank(), self.short_suit())

