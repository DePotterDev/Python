dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
my_t = (3,)
print(my_t)

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions_2 = [dimension for dimension in range(1, 12, 3)]
print(dimensions_2)
