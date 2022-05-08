players = ['charles', 'laurens', 'ingrid', 'tom', 'artois']
print(players[0:3])
print(players[:4])
print(players[:2])

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

