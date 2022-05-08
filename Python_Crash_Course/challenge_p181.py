from random import randint, choice


class Die():
    """Rolls a dice."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Rolling a dice fro 10 times between 1 and sides"""
        for roll_num in range(10):
            print(randint(1, self.sides))


# results = []
# d10 = Die(sides=10)
# d10.roll_die()

# for roll_num in range(10):
#     result = d10.roll_die()
#     results.append(result)
# print(results)

lottery = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 'l', 'a', 'u', 'r', 'e')
number = 0
print("Following letters or numbers are selected: ")
while number < 4:
    number += 1
    random = choice(lottery)
    print(f"\t{random}")








