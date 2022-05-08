alien_0 = {'color': 'green', 'ship': 'shuttle', 'planet': 'venus'}
alien_2 = {'color': 'red', 'ship': 'saucer', 'planet': 'mars'}
alien_3 = {'color': 'yellow', 'ship': 'rocket', 'planet': 'jupiter'}

aliens = [alien_0, alien_2, alien_3]

for alien in aliens:
    print(alien)
print("\n")
cards = []
# Make 54 cards.
for card in range(54):
    card = {'color': 'red', 'value': 'ace', 'category': 'spades'}
    cards.append(card)

for card in cards[:3]:
    if card['color'] == 'red':
        card['color'] = 'black'
        card['value'] = 'queen'
        card['category'] = 'hearts'


# Show first 5 cards
for card in cards[:5]:
    print(card)
print("...")

# Show how many aliens have been created.
print(f"Total number of cards: {len(cards)}")

