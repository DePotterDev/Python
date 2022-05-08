class Restaurant:
    """Restaurant with two attributes"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def describe_restaurant(self):
        """Describing restaurant"""
        print(f"{self.name.title()} serves {self.cuisine}.")

    def open_restaurant(self):
        """Describing the opening hours"""
        print(f"{self.name.title()} is open from 11:30 am till 3 pm and from 6pm till 11:30pm")

    def number_served(self):
        """Number of customers served."""
        print(f"{self.served} people served.")

    def set_number_served(self, served):
        """Set the number of people served."""
        if self.served <= served:
            self.served = served
        else:
            print("Can't decrement number.")

    def increment_number_served(self, increment):
        """Increment number"""
        self.served += increment


restaurant = Restaurant('padthai', 'thai')
# restaurant_2 = Restaurant("Raul's", 'ragu')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant_2.describe_restaurant()
restaurant.number_served()
restaurant.set_number_served(12)
restaurant.number_served()
restaurant.set_number_served(11)
restaurant.number_served()
restaurant.increment_number_served(5)
restaurant.number_served()


class Users:
    """Class with users"""
    def __init__(self, first_name, last_name):
        """Describe the users"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Describing the user"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        print(f"My name is {full_name}.")

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello, {self.first_name.title()}!")

    def increment_login_attempt(self):
        """Increment the attempt by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Login reset"""
        self.login_attempts = 0


laurens = Users('Laurens', 'de Potter')
# ingrid = Users('ingrid', 'silva de potter')
laurens.describe_user()
# ingrid.greet_user()

print(laurens.login_attempts)
laurens.increment_login_attempt()
print(laurens.login_attempts)
laurens.increment_login_attempt()
print(laurens.login_attempts)
laurens.reset_login_attempts()
print(laurens.login_attempts)





