#8-12
def make_sandwhich(*toppings):
	print(toppings)


make_sandwhich('cheese')
make_sandwhich('chicken mayo', 'bacon', 'ham')
make_sandwhich('bacon, egg and cheese', 'ham, cheese and tomato', 'dagwood')

#8-13
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('trystan', 'dames',
	location='sunninghill',
	studying='coding',
	age = 20)
	
print(user_profile)

#8-14
def make_car(brand, model, **car_info):
	car_info['brand_name'] = brand
	car_info['model_type'] = model
	return car_info

car = make_car('nissan', 'skyline',
	color='sunninghill',
	tow_package='True',
	year = 2018)
	
print(car)
