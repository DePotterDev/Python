first = 1

def place():
    global first
    print(first)
    first = 2
    print(first)

print(first)
place()
print(first)