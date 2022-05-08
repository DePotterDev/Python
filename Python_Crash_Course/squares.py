squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# More concisely
values = []
for value in range(1, 11):
    values.append(value**3)
print(values)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(f"\n{min(digits)}")
print(f"\n{max(digits)}")
print(f"\n{sum(digits)}")

# List comprehension
squares = [(value**2 + 1) for value in range(1, 11)]
print(squares)
