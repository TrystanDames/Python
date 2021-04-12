#9-4
class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"\n{self.restaurant_name.title()} is an amazing restaurant that has {self.cuisine_type} as their cuisine.")

	def open_restaurant(self):
		print(f"\n{self.restaurant_name.title()} is open and happy to give you the service you desire.")

	def set_number_served(self):
		print(f"This restaurant has served {self.number_served} many customers.")

	def update_number_served(self, customers):
		if customers >= self.number_served:
			self.number_served = customers
		else:
			print("You can't have less than 0 customers!")

	def increment_number_served(self, customer):
		self.number_served += customer

my_restaurant = Restaurant('irish rock', 'pub food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.update_number_served(149)
my_restaurant.set_number_served()
my_restaurant.increment_number_served(10)
my_restaurant.set_number_served()

#9-5
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")
