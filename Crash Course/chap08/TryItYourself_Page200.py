#8-3
def make_shirt(shirt_size, shirt_print):
	print(f"\nThe size of the shirt is {shirt_size}.")
	print(f"The writing on the shirt will be: {shirt_print}.")

make_shirt('large', 'Embers Gaming')

def make_shirt(shirt_size, shirt_print):
	print(f"\nThe size of the shirt is {shirt_size}.")
	print(f"The writing on the shirt will be: {shirt_print}.")

make_shirt(shirt_size = 'large', shirt_print = 'Embers Gaming')

#8-4
def make_shirt(shirt_print, shirt_size = 'large'):
	print(f"\nThe size of the shirt is {shirt_size}.")
	print(f"The writing on the shirt will be: {shirt_print}.")

make_shirt(shirt_print = 'I love Python')
make_shirt(shirt_size = ' medium', shirt_print = 'I love Python')
make_shirt(shirt_size = 'small', shirt_print = 'Python is fun')

#8-5
def describe_city(city, country = 'South Africa'):
	print(f"\n{city.title()} is in the country of {country}.")

describe_city(city = 'cape town')
describe_city(city = 'pretoria')
describe_city(city = 'chicago')