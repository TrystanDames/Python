#4-15
buffet = ('egg', 'beef', 'rice', 'chicken', 'potatoes')
#buffet.append(bread)
for food in buffet:
	print(food)

buffet = ('egg', 'steak', 'rice', 'lamb', 'potatoes')
print("\nModified Buffet:")
for dishes in buffet:
	print(dishes)

digits=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(digits)
print(f"The first 5 numbers in the list are {digits[0:5]}")
print(f"The middle 5 numbers in the list are {digits[8:13]}")
print(f"The end 5 numbers in the list are {digits[-5:]}")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))