def mainMenu():
	print("Choose between the 4 of which wood you would like.")
	print("1. Pine")
	print("2. Oak")
	print("3. Mahogany")
	print("4. Quit")

	selection = int (input("Enter choice: "))

	if selection == 1:

		print("1. Large Table")
		print("2. Small Table")
		select = int (input("Enter what size: "))
		if select == 1:
			largePine()

		elif select == 2:
			pine()

		else:
			print("Invalid choice")
			mainMenu()

	elif selection == 2:
		print("1. Large Table")
		print("2. Small Table")
		select = int (input("Enter what size: "))
		if select == 1:
			largeOak()

		elif select == 2:
			oak()

		else:
			print("Invalid choice")
			mainMenu()

	elif selection == 3:
		print("1. Large Table")
		print("2. Small Table")
		select = int (input("Enter what size: "))
		if select == 1:
			largeMahogany()

		elif select == 2:
			mahogany()

		else:
			print("Invalid choice")
			mainMenu()

	elif selection == 4:
		exit

	else:
		print("Invalid choice. Enter 1-4")
		mainMenu()

def largePine():
	print("You choose Pine wood. Cost- R1040")	
	anykey = input("\n Press Enter to go back to main menu.")
	mainMenu()

def pine():
	print("You choose Pine wood. Cost- R1000")	
	anykey = input("\n Press Enter to go back to main menu.")
	mainMenu()

def largeOak():
	print("You choose Oak wood. Cost- R1290")
	anykey = input("\n Press Enter to go back to main menu.")
	mainMenu()

def oak():
	print("You choose Oak wood. Cost- R1250")
	anykey = input("\n Press Enter to go back to main menu.")
	mainMenu()

def largeMahogany():
	print("You choose Mahogany wood. Cost- R1540")
	anykey = input("\n Press Enter to go back to main menu.")
	mainMenu()

def mahogany():
	print("You choose Mahogany wood. Cost- R1500")
	anykey = input("\n Press Enter to go back to main menu.")
	mainMenu()

mainMenu()