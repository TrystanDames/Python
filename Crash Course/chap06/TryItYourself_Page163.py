#6-4
language_means = {
	'for': 'This is to allow us to create a loop',
	'.pop': 'This allows us to delete something at the end of a list',
	'del': 'This allows us to delete something specific',
	'sum()': 'This allows us to sum up all the values in a variable',
	'print()': 'This allows us to see the info we put into our program',
	'backslash(n)': 'This creates a new line where this is placed',
	'backslash(t)': 'This makes an indent for where this is placed',
	'get()': 'This fetches something within the variable.'
}

print("\nThe following words and what they mean in python:")
for language in language_means.values():
	for means in language_means.keys():
		print(f"\n{means}: {language}")

#6-5
rivers = {
	'nile': 'egypt',
	'sepik': 'new guinea',
	'mississippi': 'united states'
}

for river in rivers.keys():
	for country in rivers.values():
		print(f"\nThe {river} river runs through the county of {country}")

#6-6
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
take_poll = {'jen','sarah', 'edward', 'phil', 'trystan', 'jaden', 'vusi'}

for poll in take_poll:
	if poll in favorite_languages:
		print(f"\nThank you {poll.title()} for taking the poll we really appreciate it.")
	else:
		print(f"\nWe are inviting you {poll.title()} to come and take our poll.")