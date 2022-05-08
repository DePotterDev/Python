# rental_car = input("What kind of rental car do you like? ")
# print(f"Let me see if I can find any {rental_car}!")
#
# table = input("With how many people are you? ")
# table = int(table)
# if table > 10:
#     print("You'll have to wait a bit...")
# else:
#     print("Table is free!")

number = input("Give a number: ")
number = int(number)

if number % 10 == 0:
    print("This number is a multiple of 10!")
else:
    print("This number is not a multiple of 10!")