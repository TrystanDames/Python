movies = {
	"Finding Dort": [3, 5],
	"Bourne": [18,5],
	"Tarzan": [15,5],
	"Ghost Busters": [12, 5]
}

while True:
	choice = input("What film would you like to watch?: ").strip().title()
	if choice in movies:
		age = int(input("How old are you?: ").strip())

		if age >= movies[choice][0]:
			#Check enough seats
			num_seats = movies[choice][1]

			if num_seats > 0:
				print("Enjoy the movie!")
				movies[choice][1] = movies[choice][1] - 1

			else:
				print("Sorry, we are sold out!")

		else:
			print("You are not old enough to watch this movie!")
	else:
		print("We don't have that movie...")

