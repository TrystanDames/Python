#5-3
alien_color = ['red', 'yellow']
if 'red' in alien_color:
	print("You just earned 5 points")
if '' in alien_color:
	print("You just earned 5 points")

#5-4
alien_color = ['red', 'yellow']
if 'green' in alien_color:
	print("You just earned 5 points")
else:
	print("You scored nothing")

#5-5
alien_color = ['red', 'yellow']
if 'green' in alien_color:
	print("You just earned 5 points")
elif 'red' in alien_color:
	print("You just earned 10 points")
elif 'yellow' in alien_color:
	print("You just earned 15 points")
else:
	print("You scored nothing")

#5-6
age = 12
if age < 2:
	print("Person is a baby")
elif age >= 2 and age < 4:
	print("Person is a todler")
elif age >= 4 and age < 13:
	print("Person is a kid")
elif age >= 13 and age < 20:
	print("Person is a teenager")
elif age >= 20 and age < 65:
	print("Person is an adult")
elif age >= 65:
	print("Person is an elder")

#5-7
favorite_fruits = ['oranges', 'naartjies', 'apples', 'watermelon']
if 'strawberries' in favorite_fruits:
	print("Strawberries is your favorite fruit!")
elif 'pineapple' in favorite_fruits:
	print("Pineapple is your favorite fruit!")
elif 'pricot' in favorite_fruits:
	print("Apricot is your favorite fruit!")
elif 'pear' in favorite_fruits:
	print("Pear is your favorite fruit!")
elif 'oranges' in favorite_fruits:
	print("Oranges is your favorite fruit!")
