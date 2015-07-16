# crazy_eights.py
#----------------
# by Hestiaflame
#----------------


from discard import DiscardPile
from deck import Deck
from player import CrazyEightsPlayer
from card import Card

class CrazyEights():
	
	# Create however many players you want
	def __init__(self, player_num):
		self.deck = Deck(range(52), shuffle=True)
		self.players = [CrazyEightsPlayer([self.deck.draw() for _ in range(8)]) for each_player in range(player_num)]
		self.player_num = player_num
		self.discardPile = Deck()
		self.turn_number = 0
		for player in self.players:
			player.game = self
			
	def __repr__(self):
		pass
		
	def game_is_over(self):
		""" returns T/F depending on whether the game is over"""
		for each_player in self.players:
			if each_player.empty():
				print("Player {} won the game".format(self.players.index(each_player)))
				return True
		return False

	def play(self):
		self.discardPile.add(self.deck.draw())
		print("")
		print(self.discardPile.cards)
		print("")

		while not self.game_is_over():
			self.turn()
			self.turn_number = (self.turn_number + 1) % self.player_num		


	def turn(self):
		print("")
		print("hand no {}: {}".format(self.turn_number, self.current_player().cards))
		if self.deck.empty():
			print("")
			print("RESHUFFLE")

			self.deck.add_deck(self.discardPile)
			self.discardPile.add(self.deck.draw())

			print(self.discardPile)
			print("")

		p_card = self.discardPile.peek()
		card_played = self.current_player().get_play(p_card)
		self.validate(p_card, card_played)
########
		if card_played.suit() == p_card.suit() and card_played.rank() == p_card.rank() and card_played.rank() != "8":
			print("draw")
		else:
			print(card_played)
			self.discardPile.add(card_played)

########
		
	def current_player(self):
		return self.players[self.turn_number]
		
	def validate(self, p_card, next_card):
		if p_card.rank() != next_card.rank():
			if p_card.suit() != next_card.suit():
				if next_card.rank() != "8":
########
					print("turn number {}".format(self.turn_number))
					print(next_card)
					print("")
########
					raise ValueError("Your card is invalid")


	def draw(self):
		return self.deck.draw()


#g = CrazyEights(4)
#g.play()
