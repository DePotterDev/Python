guest_list = ['Benji', 'Elon Musk', 'Hannibal Barca']

print(f"To the best boy ever, {guest_list[0]}, you are invited to the most amazing dinner party ever.")
print(f"Dear {guest_list[1]}, you are invited to a amazing dinner party.")
print(f"Dear {guest_list[2]}, you are invited to a amazing dinner party.")

cant_come = guest_list.pop(2)
guest_list.append('Joe Rogan')
can_come = guest_list[-1]
print(f"Unfortunately {cant_come}, can't make it. But {can_come} will come instead.")
print(guest_list)
guest_list.insert(0, 'Alexander The Great')
guest_list.insert(-1, 'Ebbers')
guest_list.insert(3,'Neefje')

print(guest_list)
guest_list.pop(0)
guest_list.pop(1)
guest_list.pop(-1)
guest_list.pop(-1)
print(guest_list)

print(len(guest_list))