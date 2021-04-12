#6-7
person_known = {
	'trystandames': {
		'first_name': 'trystan', 
		'last_name': 'dames', 
		'age': 20, 
		'city': 'sunninghill'
		},
	'sheldondames': {
		'first_name': 'sheldon',
		'last_name': 'dames',
		'age': 17,
		'city': 'roodepoort'
		},
	'malosemakwea': {
		'first_name': 'malose',
		'last_name': 'makwea',
		'age': 20,
		'city': 'parktown'
		},
}

for username, user_info in person_known.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first_name']} {user_info['last_name']}"
	old = user_info['age']
	location = user_info['city']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tAge: {old}")
	print(f"\tCity: {location.title()}")

#6-8
pet_0 = {
	'name': 'zeus',
	'type': 'dog',
	 'owner': 'trystan'
	 }
pet_1 = {
	'name': 'poncho',
	'type': 'cat',
	'owner': 'hannah'
}
pet_2 = {
	'name': 'ouro',
	'type': 'snake',
	'owner': 'jaden'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	for key, value in pet.items():
		print(f"\n{key.title()}:\t{value.title()}")

#6-9
favourite_places = {
	'trystan': 'durban',
	'sheldon': 'home',
	'stacey': 'cape town',
}

for person, place in favourite_places.items():	
	print(f"\n{person.title()} likes {place.title()} as their vacation spot!")

#6-10
people_numbers = {
	'trystan': [8, 7],
	'jaden': [3, 0],
	'hannah': [6, 2],
	'scott': [1, 4],
	'jaymee': [9, 5]
}

print("\nThese are people with their favourite number")
for person, num in people_numbers.items():
	print(f"\n{person.title()} --> {num}")

#6-11
cities ={
	'joburg': {
	'population': 957_441,
	'province': 'gauteng'
	},
	'cape town': {
	'population': 433_688,
	'province': 'western cape'
	},
	'pretoria': {
	'population': 741_651,
	'province': 'gauteng'
	},
}

for city, user_info in cities.items():
	print(f"\n Area: {city.title()}")
	population = user_info['population']
	province = user_info['province']

	print(f"\tPopulation: {population}")
	print(f"\tProvince: {province.title()}")

#6-12
users = {
'aeinstein': {
			'first': 'albert',
			'last': 'einstein',
			'location': 'princeton',
			},
'mcurie': {
			'first': 'marie',
			'last': 'curie',
			'location': 'paris',
			},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

class_mates = {
	'jaden': {
		'name': 'jaden',
		'laptop': 'hp',
		'school': 'code college'
	},
	'trystan': {
		'name': 'trystan',
		'laptop': 'lenovo',
		'school': 'code college'
	},
	'moabi': {
		'name': 'moabi',
		'laptop': 'acer',
		'school': 'code college'
	},
}

for classes, class_info in class_mates.items():
	print(f"\nStudent: {classes}")
	names = f"{class_info['name']}"
	laptops = f"{class_info['laptop']}"
	schools = class_info['school']
	print(f"\tName: {names.title()}")
	print(f"\tLaptop: {laptops.title()}")
	print(f"\tInstitution: {schools.title()}")