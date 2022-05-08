filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line. strip()

print(f"{pi_string[:10]}...")
print(len(pi_string))