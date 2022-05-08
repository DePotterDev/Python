filename = 'programming.txt'

# with open(filename, 'w') as file_object:
with open(filename, 'a') as file_object:
    file_object.write("I love cats\n")
    file_object.write("I love dogs.\n")
