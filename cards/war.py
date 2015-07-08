from player import WarPlayer
from deck import Deck

class War:
    	"A game of War."

    	def __init__(self):
        	"""Sets up the players and the deck for a game of war. Then deals 
       		out the cards to the players. Sets self.battles to 0. Finally, 
        	creates a battle deck for each player. This will be used in the
        	battle method."""
		self.player1 = WarPlayer()
		self.player2 = WarPlayer()
		self.battles = 0
		originalDeck = Deck(range(52), True)
		while originalDeck.count() > 0:
			self.player1.take_card(originalDeck.draw())
			self.player2.take_card(originalDeck.draw())

		self.battleDeck1 = Deck()
		self.battleDeck2 = Deck()

    	def play(self):
        	"""Plays the entire game of war until it is over, then returns an
        	int showing how many battles were in the game."""
		while not self.game_is_over():
			self.battle()
			self.battles += 1
		return self.battles
            
    	def game_is_over(self):
		"""Returns True if the game is over (if either player has no cards). 
		Otherwise returns False."""
		if not self.player1.has_any_cards() or not self.player2.has_any_cards():
			return True
		else:
			return False
        
    	def battle(self):
		""" Plays a battle between the two players. There are a few steps:
		1. Draw cards for battle (try to draw a card for each player)
		2. If the top cards in each battle deck are different, then one 
		player has won the battle. Have the winning player take both
		decks.
		3. If the top cards in each battle deck are the same, then have
		each player draw three cards for battle, and then call battle
        	again.
        	"""
#1
		if not self.game_is_over():
			self.draw_cards_for_battle()
#2	
		if self.battleDeck1.peek() > self.battleDeck2.peek():
			self.player1.take_deck(self.battleDeck1)
			self.player1.take_deck(self.battleDeck2)
		elif self.battleDeck1.peek() < self.battleDeck2.peek():
			self.player2.take_deck(self.battleDeck1)
			self.player2.take_deck(self.battleDeck2)
#3
		elif self.battleDeck1.peek() == self.battleDeck2.peek():
			for _ in range(3):
				self.draw_cards_for_battle()
			if not self.game_is_over():
				self.battle()

	def draw_cards_for_battle(self):
		if self.player1.has_any_cards():
			self.battleDeck1.add(self.player1.draw_card())
		if self.player2.has_any_cards():
			self.battleDeck2.add(self.player2.draw_card())
	

