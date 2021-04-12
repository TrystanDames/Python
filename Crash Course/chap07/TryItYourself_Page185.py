#7-4
prompt = "\nTell me what toppings you would like on your pizza:"
prompt += "\nEnter 'quit' to end the list of pizza toppings. "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)

#7-5
prompt = "\nHow old is one of the individuals so you can get the price of their movie ticket?:"
age = int(input(prompt))
if age <= 3:
	print("The ticket to the movie is free.")
elif age >= 3 and age < 12:
		print("The price of your movie ticket will be $10.")
elif age >= 15:
		print("The price of the movie ticket will be $15.")

#7-6
prompt = "\nTell me what toppings you would like on your pizza:"
prompt += "\nEnter 'quit' to end the list of pizza toppings. "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(message)