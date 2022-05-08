my_foods = ['pizza', 'stew with fries', 'sushi', 'ice-cream', 'waffles', 'chocolate', 'pita']
friends_food = my_foods[:]

my_foods.append('bananas')
friends_food.append('cornflakes')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

print(f"\nFirst three items are {my_foods[:3]}")
print(f"\nThree items from the middle are {my_foods[3:6]}")
print(f"\nLast three items are {my_foods[-3:]}")

for food in my_foods:
    print(food)

for food in friends_food:
    print(food)