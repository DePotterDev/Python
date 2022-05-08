from unittest import result
from name_function import formatted_name

print("Please enter the first and last names")
while True:
    first_name = input("Please enter the first name:")
    if first_name == "x":
        print("Ciao!")
        break

    last_name = input("Please enter the last name: ")
    if last_name == "x":
        print("Ciao!")
        break

    result = formatted_name(first_name, last_name)
    print("Formatted name is: " + result + ".")