# David Klein, 9/25/2015

def main():
	play_again = game()
	while play_again == 'again':
		play_again = game()

def game():
	play_game = ''
	# have user choose minimum and maximum
	# if not viable min or max, then end program

	import random

	try:
		minimum = int(input("Enter minimum number of sticks\n> "))
		maximum = int(input("Enter maximum number of sticks\n> "))
	except ValueError:
		print("Not viable minimum and maximum number of sticks! We'll choose something")
		minimum = 15
		maximum = 20
	# randomly choose number between minimum and maximum
	if minimum < 0 or minimum > maximum or maximum < 0:
		print("Not viable minimum and maximum number of sticks! We'll choose something")

	total_sticks = random.randint(minimum, maximum)

	# have user choose who starts first
	# if not viable input then ask again
		
	starting_player = input("Who goes first, (p)layer or (c)omputer?\n> ")

	while starting_player != "p" and starting_player != "c":
		starting_player = input("Sorry, I didn't catch that.\nWho goes first, (p)layer or (c)omputer?\n> ")

	# create variable to keep track of whose turn it is
	# turns will be kept track of so the user will play on odd numbers
	# and the computer will player on even numbers

	player_turn = 0
	
	if starting_player == "p":
		player_turn += 1           
	else:
		player_turn += 2

	# create while loop to iterate turns
	# if only 1 stick remains then the player who's turn it is will lose

	while total_sticks > 0:
		if total_sticks == 1:
			print("There is 1 stick left!")
		else:
			print("There are", total_sticks, "sticks left")
		if total_sticks == 1 and player_turn % 2 == 1:
			print("You pick up the last stick and lose :/\nBetter luck next time!")
			play_again = input("Enter 'again' to play\n> ")
			break
		elif total_sticks == 1 and player_turn % 2 == 0:
			print("The computer picks up the last stick and loses! :D\nNice job! But could you do that again?")
			play_again = input("Enter 'again' to play\n> ")
			break

		# odd numbers for turn-variable indicate a user's turn
		# ensure player will only pick 1, 2, or 3, and that they will not make unreal total stick number
		# even numbers for turn-variables indicate a computer's turn
		# ensure computer will not make total stick value become unreal
		# have computer pick 1 every time total sticks is in sequence of 2 + 4 * n
		# have computer pick 2 every time total sticks is in sequence of 3 + 4 * n
		# have computer pick 3 every time total sticks is in sequence of 4 + 4 * n
		# have computer pick random number for all other possible total sticks

		elif player_turn % 2 == 1:
			pick_up = int(input("How many sticks do you want to pick up (1 - 3)?\n> "))
			while pick_up != 1 and pick_up != 2 and pick_up != 3:
				print("I don't think that is a valid number. Let's try again.")
				pick_up = int(input("How many sticks do you want to pick up (1 - 3)?\n> "))
			if (total_sticks - pick_up) <= 0:
				print("You pick up the last stick and lose :/\nBetter luck next time!")
				play_again = input("Enter 'again' to play\n> ")
				break
			total_sticks -= pick_up
			if pick_up == 1:
				print("You pick up 1 stick")
			else:
				print("You pick up", pick_up, "sticks")
			player_turn += 1
			continue
		else:
			if total_sticks in range(2, maximum+1, 4):
				pick_up = 1
			elif total_sticks in range(3, maximum+1, 4):
				pick_up = 2
			elif total_sticks in range(4, maximum+1, 4):
				pick_up = 3
			else:
				pick_up = random.randint(1, 3)
			total_sticks -= pick_up
			if pick_up == 1:
				print("The computer picks up 1 stick")
			else:
				print("The computer picks up", pick_up, "sticks")
			player_turn += 1
			continue
			
	return play_again

main()
