file_path = 'text_files/naam.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()


for line in lines:
    print(f"\t{line.rstrip()}")

#     contents = file_object.read()
# print(contents.rstrip())