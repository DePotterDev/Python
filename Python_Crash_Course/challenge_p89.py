current_usernames = ['admin', 'user1', 'user2', 'user3', 'user4', 'user5']
new_usernames = ["John", "Michael", "Pam", "Ron", "UseR3"]

if current_usernames:
    for username in current_usernames:
        if username == 'admin':
            print("Hello, admin, welcome back, now get to work!")
        else:
            print(f"Welcome back {username}!")
    print("\nEnd program")
else:
    print("No users found.")


for new_username in new_usernames:
    if new_username.lower() in current_usernames:
        print(f"Username {new_username} has been taken, please enter other usename.")
    else:
        print(f"Username {new_username} available")

print("\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        ordinal = 'st'
    elif number == 2:
        ordinal = 'nd'
    elif number == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    print(f"{number}{ordinal}")
