# game.py
# -------
# by Hestiaflame
# Will hopefully simulate a game of crazy eights.

"""
does not work yet!!!
"""

from player import Player
from deck import Deck

deck = Deck()
deck.mix()

player1 = Player([deck.draw() for each_number in range(8)])
player2 = Player([deck.draw() for each_number in range(8)])
player3 = Player([deck.draw() for each_number in range(8)])
player4 = Player([deck.draw() for each_number in range(8)])

print("")
print("Player1's hand: {}".format(player1.cards))
print("Player2's hand: {}".format(player2.cards))
print("Player3's hand: {}".format(player3.cards))
print("Player4's hand: {}".format(player4.cards))
print("")


def play(turn):
	if turn == 1:
		turn += 1
		for each_card in player1.cards:
			if each_card.suit() == prev_card.suit() or each_card.rank() == prev_card.rank():
				index_return = player1.cards.index(each_card)
				return player1.play(index_return)
			else:
				player1.add(deck.draw())

	if turn == 2:
		turn += 1
		for each_card in player2.cards:
			if each_card.suit() == prev_card.suit() or each_card.rank() == prev_card.rank():
				index_return = player2.cards.index(each_card)
				return player2.play(index_return)
			else:
				player2.add(deck.draw())
	if turn == 3:
		turn += 1
		for each_card in player2.cards:
			if each_card.suit() == prev_card.suit() or each_card.rank() == prev_card.rank():
				index_return = player2.cards.index(each_card)
				return player2.play(index_return)
			else:
				player2.add(deck.draw())
	if turn == 4:
		turn = 1
		for each_card in player4.cards:
			if each_card.suit() == prev_card.suit() or each_card.rank() == prev_card.rank():
				index_return = player4.cards.index(each_card)
				return player4.play(index_return)
			else:
				player4.add(deck.draw())
		

prev_card = deck.draw()
turn = 1

while True:
	if player1.empty() == True:
		print("Player 1 won the game")
		break
	elif player2.empty() == True:
		print("Player 2 won the game")
		break
	elif player3.empty() == True:
		print("Player 3 won the game")
		break
	elif player4.empty() == True:
		print("Player 4 won the game")
		break
	else:
		print("")
		prev_card = play(turn)
		print(prev_card)
		print("")
