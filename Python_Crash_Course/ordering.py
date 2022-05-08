countries = ['Belgium', 'France', 'Australia', 'England', 'USA', 'Japan', 'Netherlands', 'Brazil', 'Peru', 'Hungary', 'South-Korea']
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

# Sorting without changing the order

flowers = ['Rose', 'Tulip', 'Sunflower', 'Daisy', 'Lily', 'Mayflower']

print("\nHere is a list of flowers:")
print(flowers)

print("\nHere is a sorted list:")
print(sorted(flowers))

print("\nHere is a the original list:")
print(flowers)

# Reverse non-alphabetically
print("\nHere is a reversed list:")
flowers.reverse()
print(flowers)

