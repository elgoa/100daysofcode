import random

enemy_draw = random.randint(1,3)
own_draw = int(input("Was Wählst du (1 für Schere, 2 für Stein, 3 für Papier): "))

print(enemy_draw)
if(own_draw > enemy_draw ): 
	print("du hast gewonnen!")

elif( own_draw == 1 and enemy_draw == 3):
	print("du hast gewonnen!")

elif(own_draw == enemy_draw):
	print("es ist unentschieden")

else:
	print("du hast verloren")