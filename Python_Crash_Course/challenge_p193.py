filename = 'guest.txt'
filename_2 = 'guest_book.txt'
poll = 'programming_poll.txt'


name = input("Please enter your name: ")

with open(filename, 'w') as file_object:
    file_object.write(name)

with open(filename_2, 'w') as file_object_2:
    print("\nWelcome in the Holiday Inn, please enter your name: ")
    print("Write 'exit' to exit program.")

    active = True

    while active:
        name = input("\tYour name: ")
        if name == 'exit':
            active = False
        else:
            file_object_2.write(f"{name}\n")

with open(poll, 'a') as file_poll:
    print("\nWelcome to the poll! ** TO QUIT, TYPE 'stop' **")
    print("What do you like about programming?")

    active = True
    while active:
        answer = input("\tAnswer: ")
        if answer == 'stop':
            active = False
        else:
            file_poll.write(f"{answer}\n")





