import json


def check_number():
    """Checking if the number is inside the favorite number file"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def new_number():
    filename = 'favorite_number.json'
    number = input("What is your favorite number: ")
    with open(filename, 'w') as f2:
        json.dump(number, f2)
    return number


def favorite_number():
    number = check_number()
    if number:
        print(f"I know your favorite number! It's {number}!")
    else:
        fav_number = new_number()
        print(f"Your favorite number is {fav_number}")


favorite_number()