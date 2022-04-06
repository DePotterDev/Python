from typing_extensions import Self
from unicodedata import name


class Pizza:

    print("Welcome to Mamamia")

    def __init__(self, dough, topping_1, topping_2=None):
        self.dough = dough
        self.topping_1 = topping_1
        self.topping_2 = topping_2
        
    def baking(self):
        if self.topping_2:
            return f"Making a {self.dough} pizza with {self.topping_1} and {self.topping_2}."
        else:
            return f"Making a {self.dough} pizza with {self.topping_1}."
    def name(self):
        if self.topping_1 == "cheese" and self.topping_2 == "pineapple":
            return "pizza hawai"
        else:
            return "not a pizza"


class RestoBrugge(Pizza):
    def delivery(self, location="Brugge"):
        pizza = self.name()
        return f"delivering {pizza} to {location}"

        



pizza1 = Pizza("thick crust", "mozzarela", "pepperoni")
print(pizza1.topping_1)
print(pizza1.baking())
pizza1.topping_1 = "cheese"
print(pizza1.baking())
pizza1 = Pizza("thin crust", "pineapple")

resto = RestoBrugge("thin crust", "cheese", "pineapple")
print(resto.delivery())