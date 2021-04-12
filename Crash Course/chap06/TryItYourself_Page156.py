#6-1
person_known = {'first_name': 'trystan', 'last_name': 'dames', 'age': 20, 'city': 'sunninghill'}
print(person_known['first_name'].title())
print(person_known['last_name'].title())
print(person_known['age'])
print(person_known['city'].title())

#6-2
people_numbers = {
	'trystan': 8,
	'jaden': 3,
	'hannah': 6,
	'scott': 1,
	'jaymee': 9,
}
favorite = people_numbers['trystan']
print(f"Trystan's favourite number is {favorite}.")

favorite = people_numbers['jaden']
print(f"Jaden's favourite number is {favorite}.")

favorite = people_numbers['hannah']
print(f"Hannah's favourite number is {favorite}.")

favorite = people_numbers['scott']
print(f"Scott's favourite number is {favorite}.")

favorite = people_numbers['jaymee']
print(f"Jaymee's favourite number is {favorite}.")

#6-3
language_means = {
	'for': 'This is to allow us to create a loop',
	'.pop': 'This allows us to delete something at the end of a list',
	'del': 'This allows us to delete something specific',
	'sum()': 'This allows us to sum up all the values in a variable',
	'print()': 'This allows us to see the info we put into our program'
}

means = language_means['for']
print(f"This is what for means:\n\t{means}")

means = language_means['.pop']
print(f"This is what .pop means:\n\t{means}")

means = language_means['del']
print(f"This is what del means:\n\t{means}")

means = language_means['sum()']
print(f"This is what sum() means:\n\t{means}")

means = language_means['print()']
print(f"This is what print() means:\n\t{means}")