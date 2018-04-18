import time

print("Hello new gamer !!")
print("If you launched this script, it should be, because you don't know what to play, right ?")
time.sleep(3)
print("And I'm gonna help you ;) .")
time.sleep(3)
print("I'm going to ask you some questions, answer by 'yes' or 'no'.")
time.sleep(3)
print("Let's go !")
an = raw_input("Do you want to avoid using much of your brain ?\n")
if an == "yes":
	an = raw_input("Are your reflexes good ?\n")
	if an == "yes":
		an = raw_input("Do you want to point and click click click... ?\n")
		if an == "yes":
			an = raw_input("Do you plan on playing for the next week straight?\n")
			if an == "yes":
				print("In this case, the perfect game for you is :")
				print("World Of Warcraft !")
			else:
				print("In this case, the perfect game for you is :")
				print("Diablo 2 !")
		else:
			an = raw_input("Do you want the harvest game ever ?\n")
			if an == "yes":
				print("In this case, the perfect game for you is :")
				print("Devil May Cry 3 !")
			else:
				print("In this case, the perfect game for you is :")
				print("Monkey Ball !")
	else:
		an = raw_input("Are you on drugs ?\n")
		if an == "yes":
			print("In this case, the perfect game for you is :")
			print("REZ !")
		else:
			an = raw_input("Do you want to feel like you are ?\n")
			if an == "yes":
				print("In this case, the perfect game for you is :")
				print("Geometry Wars 2 !")
			else:
				an = raw_input("Do you have a good timing ?\n")
				if an == "yes":
					an = raw_input("Do you want to rock ?\n")
					if an == "yes":
						print("In this case, the perfect game for you is :")
						print("Rockband 3 !")
					else:
						print("In this case, the perfect game for you is :")
						print("Irakuga !")
				else:
					an = raw_input("Are 2 buttons too many for you ?\n")
					if an == "yes":
						print("In this case, the perfect game for you is :")
						print("Pac-Man !")
					else:
						print("In this case, the perfect game for you is :")
						print("Punch-Out !")
else:
	an = raw_input("Maximum creativity ?\n")
	if an == "yes":
		print("In this case, the perfect game for you is :")
		print("Minecraft !")
	else:
		an = raw_input("Do you want to solve some puzzles ?\n")
		if an == "yes":
			an = raw_input("Do you feel the need for a storyline as well ?\n")
			if an == "yes":
				an = raw_input("Are you an Edward Gorey fan ?\n")
				if an == "yes":
					print("In this case, the perfect game for you is :")
					print("Limbo !")
				else:
					an = raw_input("Looking for crazy Japanese awsomeness ?\n")
					if an == "yes":
						print("In this case, the perfect game for you is :")
						print("Kataman Damacy !")
					else:
						an = raw_input("Do you want some shiny textures or indi magic ? (please answer by 'indi' or 'shiny')\n")
						if an == "indi":
							print("In this case, the perfect game for you is :")
							print("Braid !")
						if an == "shiny":
							print("In this case, the perfect game for you is :")
							print("Portal 2 !")
			else:
				an = raw_input("Kick it oldschool ?\n")
				if an == "yes":
					print("In this case, the perfect game for you is :")
					print("Tetris !")
				else:
					print("In this case, the perfect game for you is :")
					print("Lumines !")
		else:
			an = raw_input("Do you enjoy simulations ?\n")
