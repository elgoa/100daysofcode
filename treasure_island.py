print("Welcome to Treasure Island. Your mission is to find the treasure")
way = input("you want to go left or right? : ")
if(way == "left"):
	way2 = input("you want to swim or to wait: ")
	if(way2 == "wait"):
		door = input("which door you want to choose: ")
		if (door == "Red"):
			print("Burned by fire. Game over.")
		elif(door == "Yellow"):
			print("You win!")
		elif(door == "Blue"):
			print("you are eaten by a troll. Gameover.")
		else:
			print("Game Over.")
	else:
		print("You are attacked ba a trout. Game over.")

else:
	print("you fall into a hole. Game over")
	