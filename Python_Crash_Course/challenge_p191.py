

with open('text_files/learning_python.txt') as file_object:
    lines = file_object.readlines()
    print("First:")
    for line in lines:
        line = line.strip()
        print(f"\t{line.replace('python', 'java')}")


python_list = ''
for line in lines:
    python_list += line.strip()

# # print("\nSecond:")
# # # print(lines)
# print("\nThird:")
# # print(python_list)
print(python_list.replace('python', 'java'))