motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

motorcycles[0] = 'Ducati'
print(motorcycles)

# Add to the end of the list
motorcycles.append('Honda')
print(motorcycles)

cars = []
cars.append('Focus')
cars.append('Cerato')
cars.append('TR4')
cars.append('C5 Lounge')
print(cars)

cars.insert(3, 3008)
print(cars)

cars.insert(0, 'Fiesta')
print(cars)

del cars[0]
print(cars)

del cars[-1]
print(cars)

popped_cars = cars.pop()
print(cars)
print(popped_cars)

cars.append('Jimny')
cars.append('Versa')
cars.append('Sentra')
print(cars)

last_owned = cars.pop()
print(f"The last car I owned was a {last_owned.upper()}.")

first_owned = cars.pop(0)
print(f"The first car I owned was a {first_owned.upper()}.")

cars.remove('Versa')
print(cars)

cars.append('Civic')
print(cars)
too_expensive = 'Civic'
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive.upper()} is too expensive for me.")



