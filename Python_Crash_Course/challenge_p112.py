names_list_1 = {
    'jan': 15,
    'tim': 55,
    'hans': 88,
    'tom': 45,
    'amelie': 48,
}

names_list_2 = {
    'maurice': 41,
    'rene': 45,
    'artois': 99,
    'monet': 64
}

people = [names_list_1, names_list_2]

for name_list in people:
    for names, age in name_list.items():
        print(f"{names.title()} is {age} years old.")


pets_1 = {
    'maurice': {
        'pet': 'dog',
        'owner': 'john',
    },
    'patrick': {
        'pet': 'starfish',
        'owner': 'beau',
    },
    'monice': {
        'pet': 'walrus',
        'owner': 'danny',
    },
}

pets_2 = {
    'wally': {
        'pet': 'parrot',
        'owner': 'daniel',
    },
    'zorro': {
        'pet': 'cat',
        'owner': 'laurens'
    },
}

pets = [pets_1, pets_2]

for pet in pets:
    for name, details in pet.items():
        print(f"\n{details['owner'].title()} has as a pet a {details['pet']}, called {name}.")


cities = {
    'sao paulo': {
        'pop': 17,
        'country': 'brazil',
        'fact': 'largest south-american city',
    },
    'bruges': {
        'pop': 0.3,
        'country': 'belgium',
        'fact': 'is a historic city',
    },
    'barcelona': {
        'pop': 2,
        'country': 'spain',
        'fact': 'has many free museums'
    }
}

for city, details in cities.items():
    population = details['pop']
    country = details['country'].title()
    fact = details['fact']
    city = city.title()
    print(f"\nDid you know that {city} lay's in {country}, and that {city} {fact}")








