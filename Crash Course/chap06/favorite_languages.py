favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# language1 = favorite_languages.get('john', 'No point value assigned.')
# print(language1)

for key, value in favorite_languages.items():
	print(f"Key: {key.title()}, Value: {value.title()}")

print("\nAccessing keys:")
for key in favorite_languages.keys():
	print(f"Key: {key.title()}")

print("\nAccessing values:")
for value in favorite_languages.values():
	print(f"Value: {value.title()}")

fav_games = {
	'trystan': 'cod',
	'jaden': 'log',
	'scott': 'fortnite',
	'mitch': 'apex'
}

for key, value in fav_games.items():
	print(f"Key: {key.title()}, Value: {value.title()}")

print("\nAccessing keys:")
for key in fav_games.keys():
	print(f"Key: {key.title()}")

print("\nAccessing values:")
for value in fav_games.values():
	print(f"Value: {value.title()}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

