import csv
import requests


planet_list = []
with open('planets.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        planet_list.append(row[0].strip())

# bad example
# x = 1
# for planet in planet_list:
#     print(x, planet)
#     x = x + 1

# good example
for index, planet in enumerate(planet_list, start=1):
    print(index, planet)