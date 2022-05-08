message = 'add new topping: '

active = True
print("Write the toppings you want to add to your pizza.")
print("If you want to exit the program, write 'quit.")

while active:
    topping = input(message)
    if topping == 'quit':
        active = False
    else:
        print(f"Topping {topping} added to the pizza.")

movie_ticket = input("Please enter your age: ")
movie_ticket = int(movie_ticket)

if movie_ticket < 3:
    price = 0
elif movie_ticket < 12:
    price = 10
else:
    price = 15

print(f"The admission costs ${price}.")

print(f"\n Write 'quit' or python to stop the program")


while True:
    animal = input("Which animal do you like: ")
    if animal == ('python' or 'quite'):
        break
    else:
        print(f"A {animal.title()} is a very cool animal!")




