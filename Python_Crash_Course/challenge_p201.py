
active = True
print("CALCULATOR \n** enter 'q' to stop program.**")

while active:
    # While loop for calculator
    num1 = input("First number: ")
    if num1 == 'q':
        break
    num2 = input("Second number: ")
    if num2 == 'q':
        break
    try:
        total = int(num1) * int(num2)
    except ValueError:
        print("Needs to be numbers!")
    else:
        print(total)


