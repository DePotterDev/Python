user ={'name': 'Laurens', 'last name': 'de Potter de ten Broeck', 'city': 'sao paulo', }

print(user["name"])
print(user['last name'])
print(user['city'])

favorite_numbers = {
    'sarah': 5,
    'tom': 15,
    'john': 25,
    'mona': 36,
    'moniq': 36,
    'max': 36,
    'laurens': 99,
    'frida': 78,
}

print(f"{favorite_numbers['tom']}\n")

for favorite in set(favorite_numbers.values()):
    print(favorite)


capitals = {
    'brazil': 'Brasilia',
    'belgium': 'brussel',
    'nederland': 'amsterdam',
    'poland': 'warsaw',
    'chile': 'santiago',
}

more_capitals = ['rome', 'berlin']

for capital in more_capitals:
    if capital not in capitals.keys():
        print(f"{capital.title()} is not in the list!")


for country in capitals.keys():
    capital = capitals[country].title()
    country = country.title()
    print(f"The capital of {country} is {capital}.")