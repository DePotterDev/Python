requested_topping_anchovis = 'mushrooms'

if requested_topping_anchovis != 'anchovies':
    print("Hold the anchovies")

requested_toppings =['peppers', 'corn', 'mozzarella', 'tomatoes', 'bacon']
if 'peppers' in requested_toppings:
    print('Eyo, peppies!')
if 'pepperoni' in requested_toppings:
    print("Pepperoni.")
if 'bacon' in requested_toppings:
    print('Delish, bacon.')

for requested_topping in requested_toppings:
    if requested_topping == 'peppers':
        print("Sorry there ain't no peppies left!")
    else:
        print(f"{requested_topping} added to the pizza.")

empty_toppings = []

if empty_toppings:
    for empty_topping in empty_toppings:
        print(f"Your topping is {empty_topping}")
else:
    print("No toppings selected.")