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


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        """Overriding Restaurant class"""
        super().__init__(name, cuisine)
        self.flavors = "Madagascar Vanilla, Peanut Butter Caramel, Caramelized Apple with Cognac," \
                       " Chocolate Chip Brownie"

    def display_flavors(self):
        print(f"These are the available flavors: {self.flavors}")


BeachIceCream = IceCreamStand('SnowCone', 'IceCream Shop')
BeachIceCream.display_flavors()
BeachIceCream.describe_restaurant()


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


class Privileges:
    def __init__(self, privileges=['can post']):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Will show all privileges of the administrator"""
        print(f"Following privileges are added.")
        for privilege in self.privileges:
            print(f"\t-{privilege}")


class Admin(Users):
    """Admin control area"""

    def __init__(self, first_name, last_name):
        """Overriding this."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


user_2 = Admin('Laurens', 'de Potter')
user_2.describe_user()
user_2.privileges.show_privileges()

# laurens = Users('Laurens', 'de Potter')
# laurens.describe_user()

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """And the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Is added to explain how overriding works."""
        print("Need to fill the gas tank")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery")

    def testing(self):
        """This is a test to understand more about instances as attributes"""
        print(f"Hello, this is a test.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            print("Battery size upgraded!")
            self.battery_size = 100
        else:
            print("Unnecessary to change battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to electric vehicles.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks, overriding method."""
        print("This car doesn't need a gas tank!")


new_electric_car = ElectricCar('nissan', 'nitro', 2020)
new_electric_car.battery.get_range()
new_electric_car.battery.upgrade_battery()
new_electric_car.battery.get_range()
