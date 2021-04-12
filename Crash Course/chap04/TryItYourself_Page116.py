#4-10
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(digits)
print(f"The first 5 numbers in the list are {digits[0:5]}")
print(f"The middle 5 numbers in the list are {digits[8:13]}")
print(f"The end 5 numbers in the list are {digits[-5:]}")

#4-11
pizza = ['mexicana', 'bacon and avo', 'regina']
friend_pizzas = pizza[:]
pizza.append('chicken mayo')
friend_pizzas.append('vegetarian')

for food in pizza[:]:
	print(f"My favorite pizzas are: {food}")

for friend in friend_pizzas[:]:
	print(f"My friends favorite pizzas are: {friend}")