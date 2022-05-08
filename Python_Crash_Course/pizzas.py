pizzas = ['Margarita', 'Meatballs', 'Bacon & Mozzarella']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("Those are my favorite pizzas.")


friends_pizzas = pizzas[:]
friends_pizzas.append("calzoni")
pizzas.append('pepperoni')

print(pizzas)
print(friends_pizzas)

animals = ['Chicken', 'Cats', 'Dogs']

for animal in animals:
    print(f"I would like to own a {animal}")
print("Those are some great animals!")