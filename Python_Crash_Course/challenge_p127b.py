dream_vacations = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    dream_vacations[name] = destination
    polling_false = input("Do you want to continue adding locations?(yes/no) ")
    if polling_false == 'no':
        polling_active = False

print("--- Polling Results ---")
for name, destination in dream_vacations.items():
    print(f"\t{name.title()} dream vacation is {destination.title()}. ")
