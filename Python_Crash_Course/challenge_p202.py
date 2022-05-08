filename = ['text_files/cats.txt', 'text_files/dogs.txt', 'file.txt']


for file in filename:
    try:
        with open(file) as new_file:
            lines = new_file.read()
    except FileNotFoundError:
        # print("File not found!")
        pass
    else:
        print(lines)


