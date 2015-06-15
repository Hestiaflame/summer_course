# player.py
# -------
# by Hestiaflame

class Player():
    	"A player in a card game"

	def __repr__(self):
		return "<player>"

	def __init__(self, hand):
		self.cards = hand

# Play a card - give it an int that corresponds to the place in cards of the card you want to play.
# ex: p = Player([<AS>, <2H>, <8D>, <5D>, <10D>, <KH>, <6C>, <KC>])
# p.cards : [<AS>, <2H>, <8D>, <5D>, <10D>, <KH>, <6C>, <KC>]
# p.play(2) : <8D>
	def play(self, card):
		to_play = self.cards.pop(card)
		return to_play

	def add(self, card):
		self.cards.append(card)

	def empty(self):
		if len(self.cards) == 0:
			return True
		else:
			return False
