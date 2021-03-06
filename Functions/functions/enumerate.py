import csv


planet_list = []
with open('../src/planets.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        planet_list.append(row[0].strip())

# good example
for index, planet in enumerate(planet_list, start=1):
    print(index, planet)

# bad example
# x = 1
# for planet in planet_list:
#     print(x, planet)
#     x = x + 1