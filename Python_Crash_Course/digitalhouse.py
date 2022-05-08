numbers = 10
hash_number = 1

while numbers > 0:
    spaces = " " * (numbers - 1)
    hashes = "#" * hash_number
    print(spaces, hashes)
    numbers -= 1
    hash_number += 1


