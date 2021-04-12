#9-1
class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"\n{self.restaurant_name.title()} is an amazing restaurant that has {self.cuisine_type} as their cuisine.")

	def open_restaurant(self):
		print(f"\n{self.restaurant_name.title()} is open and happy to give you the service you desire.")

my_restaurant = Restaurant('irish rock', 'pub food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#9-2
class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"\n{self.restaurant_name.title()} is an amazing restaurant that has {self.cuisine_type} as their cuisine.")

	def open_restaurant(self):
		print(f"\n{self.restaurant_name.title()} is open and happy to give you the service you desire.")

my_restaurant = Restaurant('irish rock', 'pub food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('hogshead', 'pub food')
your_restaurant.describe_restaurant()

his_restaurant = Restaurant('papachinos', 'pizza')
his_restaurant.describe_restaurant()

#9-3
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()