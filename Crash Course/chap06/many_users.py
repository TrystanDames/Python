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