#7-1 
prompt = "If you tell us what you are looking for maybe I can help."
prompt += "\nWhat car are you looking for? "
cars = input(prompt)
print(f"\nLet me see if I can find a {cars.title()} for you!")

#7-2
prompt = "How many people are in your group?"
number = int(input(prompt))
if number >= 8:
	print("Sorry, you will have to wait for a table.")
else:
	print("Your table is ready and waiting for you.")

#7-3
prompt = 'Give a number that is a multiple of 10.'
number = int(input(prompt))
if number % 10 == 0:
	print(f"\n{number} is a multiple of 10")
else:
	print(f"\n{number} is not a multiple of 10")