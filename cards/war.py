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
#		print("________________________________________________________")
#		print(originalDeck)
#		print("________________________________________________________")
		while originalDeck.count() > 0:
			self.player1.take_card(originalDeck.draw())
			self.player2.take_card(originalDeck.draw())

		self.battleDeck1 = Deck()
		self.battleDeck2 = Deck()

    	def play(self):
        	"""Plays the entire game of war until it is over, then returns an
        	int showing how many battles were in the game."""
#		print("cards: {} discard: {}".format(self.player1.cards, self.player1.discardPile))
#		print("cards: {} discard: {}".format(self.player2.cards, self.player2.discardPile))
		while not self.game_is_over():
			self.battle()
			self.battles += 1
		return self.battles
            
    	def game_is_over(self):
		"""Returns True if the game is over (if either player has no cards). 
		Otherwise returns False."""
		if not self.player1.has_any_cards():
#			print("Player2 won!")
			return True
		elif not self.player2.has_any_cards():
#			print("Player1 won!")
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
		if not self.game_is_over():
	
#1
			card1 = self.player1.draw_card()
			self.battleDeck1.add(card1)

			card2 = self.player2.draw_card()
			self.battleDeck2.add(card2)

#			print("battleDeck1: {} battleDeck2: {}".format(self.battleDeck1.cards, self.battleDeck2.cards))


#2	
			if card1 > card2:
				self.player1.take_deck(self.battleDeck1)
				self.player1.take_deck(self.battleDeck2)
#				print("1cards: {}\n 1discard: {}".format(self.player1.cards, self.player1.discardPile))
#				print("2cards: {}\n 2discard: {}".format(self.player2.cards, self.player2.discardPile))
#				print("")
			elif card1 < card2:
				self.player2.take_deck(self.battleDeck1)
				self.player2.take_deck(self.battleDeck2)
#				print("1cards: {}\n 1discard: {}".format(self.player1.cards, self.player1.discardPile))
#				print("2cards: {}\n 2discard: {}".format(self.player2.cards, self.player2.discardPile))
#				print("")
#3
			else:
#				print("draw for battle")
				self.draw_cards_for_battle()
#				print("1battle: {}\n 2battle: {}".format(self.battleDeck1, self.battleDeck2))
#				print("1cards: {}\n 1discard: {}".format(self.player1.cards, self.player1.discardPile))
#				print("2cards: {}\n 2discard: {}".format(self.player2.cards, self.player2.discardPile))
#				print("")
	
	def draw_cards_for_battle(self):
       	 	""" Tries to draw one card from each player into that player's battle
        	deck. If the player has no more cards, no card is drawn. """
		for _ in range(3):
			if self.player1.has_any_cards():
				self.battleDeck1.add(self.player1.draw_card())
			if self.player2.has_any_cards():
				self.battleDeck2.add(self.player2.draw_card())

	

