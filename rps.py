import random as rand

while True:
	player_move = input("Pick your move: ")

	chance = rand.randint(1,3)
	ai_move = ""
	result = ""

	if (chance == 1):
		ai_move = "rock"
	if (chance == 2):
		ai_move = "paper"
	if (chance == 3):
		ai_move = "scissors"

	if (player_move != "rock" or player_move != "Rock" or player_move != "paper" or player_move != "Paper" or player_move != "scissors" or player_move != "Scissors"):
		result = "Invalid Move"
	if (player_move == "Rock" or player_move == "rock" and ai_move == "scissors"):
		result = "You Win"
	if (player_move == "Rock" or player_move == "rock" and ai_move == "paper"):
		result = "You Lose"
	if (player_move == "Rock" or player_move == "rock" and ai_move == "rock"):
		result = "Draw"

	if (player_move == "Paper" or player_move == "paper" and ai_move == "scissors"):
		result = "You Lose"
	if (player_move == "Paper" or player_move == "paper" and ai_move == "paper"):
		result = "Draw"
	if (player_move == "Paper" or player_move == "paper" and ai_move == "rock"):
		result = "You Win"

	if (player_move == "Scissors" or player_move == "scissors" and ai_move == "scissors"):
		result = "Draw"
	if (player_move == "Scissors" or player_move == "scissors" and ai_move == "paper"):
		result = "You Win"
	if (player_move == "Scissors" or player_move == "scissors" and ai_move == "rock"):
		result = "You Lose"

	print(result)
	continue