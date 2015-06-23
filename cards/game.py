# game.py
# -------
# by Hestiaflame

"Does not work yet!!!"

from player import Hand
from deck import Deck
from random import randint

deck = Deck()
deck.mix()

player1 = Hand([deck.draw() for each_number in range(8)])
player2 = Hand([deck.draw() for each_number in range(8)])
player3 = Hand([deck.draw() for each_number in range(8)])
player4 = Hand([deck.draw() for each_number in range(8)])

prev_card = deck.draw()
print(prev_card)
suit_to_play = prev_card.suit()
rank_to_play = prev_card.rank()
crazy = "no"
turn = 0

print("")
print("Player1's hand: {}".format(player1.cards))
print("Player2's hand: {}".format(player2.cards))
print("Player3's hand: {}".format(player3.cards))
print("Player4's hand: {}".format(player4.cards))
print("")


def crazy_eight():
	new_suit = randint(0, 3)
	if new_suit == 0:
		suit_to_play = "Clubs"
	elif new_suit == 1:
		suit_to_play = "Diamonds"
	elif new_suit == 2:
		suit_to_play = "Hearts"
	elif new_suit == 3:
		suit_to_play = "Spades"
	rank_to_play = each_card.rank()
	print("Crazy eight!!!")
	print("The new suit is {}".format(suit_to_play))



def play(turn):
	print(turn)
	if turn == 1:
		for each_card in player1.cards:
			crazy = "no"
			if each_card.suit() == suit_to_play and each_card.rank() != "8":
				index_return = player1.cards.index(each_card)
				return player1.use(index_return)
			elif  each_card.rank() == rank_to_play and each_card.rank() != "8":
				index_return = player1.cards.index(each_card)
				return player1.use(index_return)

		for each_card in player1.cards:
			if each_card.rank == "8":
				crazy_eight()
				crazy = "yes"
				index_return = player1.cards.index(each_card)
				return player1.use(index_return)
		player1.add(deck.draw())

	if turn == 2:
		for each_card in player2.cards:
			crazy = "no"
			if each_card.suit() == suit_to_play and each_card.rank() != "8":
				index_return = player2.cards.index(each_card)
				return player2.use(index_return)
			elif  each_card.rank() == rank_to_play and each_card.rank() != "8":
				index_return = player2.cards.index(each_card)
				return player2.use(index_return)
		for each_card in player2.cards:
			if each_card.rank == "8":
				crazy_eight()
				crazy = "yes"
				index_return = player2.cards.index(each_card)
				return player2.use(index_return)

		player2.add(deck.draw())


	if turn == 3:
		for each_card in player3.cards:
			crazy = "no"
			if each_card.suit() == suit_to_play and each_card.rank() != "8":
				index_return = player3.cards.index(each_card)
				return player3.use(index_return)
			elif  each_card.rank() == rank_to_play and each_card.rank() != "8":
				index_return = player3.cards.index(each_card)
				return player3.use(index_return)

		for each_card in player3.cards:
			if each_card.rank == "8":
				crazy_eight()
				crazy = "yes"
				index_return = player3.cards.index(each_card)
				return player3.use(index_return)

		player3.add(deck.draw())

	if turn == 0:
		for each_card in player4.cards:
			crazy = "no"
			if each_card.suit() == suit_to_play and each_card.rank() != "8":
				index_return = player4.cards.index(each_card)
				return player4.use(index_return)
			elif  each_card.rank() == rank_to_play and each_card.rank() != "8":
				index_return = player4.cards.index(each_card)
				return player4.use(index_return)

		for each_card in player4.cards:
			if each_card.rank == "8":
				crazy_eight()
				crazy = "yes"
				index_return = player4.cards.index(each_card)
				return player4.use(index_return)
		player4.add(deck.draw())

	print("draw")
	return prev_card


while True:
	if player1.count() == 0:
		print("Player 1 won the game")
		break
	elif player2.count() == 0:
		print("Player 2 won the game")
		break
	elif player3.count() == 0:
		print("Player 3 won the game")
		break
	elif player4.count() == 0:
		print("Player 4 won the game")
		break
	else:
		print("")
		turn = (turn + 1) % 4
		prev_card = play(turn)
		if crazy == "no":
			suit_to_play = prev_card.suit()
			rank_to_play = prev_card.rank()
		print(prev_card)
		print("")

