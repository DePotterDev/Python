# Dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"\nYou earned {new_points} points!")

# Adding dictionary values
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)

# Modifying values
alien_2 = {'color':'blue'}
print(f"\nThe alien is {alien_2['color']}.")
alien_2['color'] = 'yellow'
print(f"The alien color is now {alien_2['color']}.")

alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points': 25}
print(f"\nOriginal position: {alien_3['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_3['speed'] == "slow":
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

#The new position of the alien is:
alien_3['x_position'] = alien_3['x_position'] + x_increment
print(f"New position: {alien_3['x_position']}")

print(f"\n{alien_3}")
del alien_3['points']
print(alien_3)