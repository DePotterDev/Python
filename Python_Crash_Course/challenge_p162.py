class Restaurant:
    """Restaurant with two attributes"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describing restaurant"""
        print(f"{self.name.title()} serves {self.cuisine}.")

    def open_restaurant(self):
        """Describing the opening hours"""
        print(f"{self.name.title()} is open from 11:30 am till 3 pm and from 6pm till 11:30pm")


restaurant = Restaurant('padthai', 'thai')
restaurant_2 = Restaurant("Raul's", 'ragu')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_2.describe_restaurant()

class Users:
    """Class with users"""
    def __init__(self, first_name, last_name):
        """Describe the users"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describing the user"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        print(f"My name is {full_name}.")

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello, {self.first_name.title()}!")


laurens = Users('Laurens', 'de Potter')
ingrid = Users('ingrid', 'silva de potter')
laurens.describe_user()
ingrid.greet_user()