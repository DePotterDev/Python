sandwich_orders = ['pastrami', 'cheese', 'ham', 'pastrami', 'ham & cheese', 'salami', 'mozzarella', 'pastrami']
finished_sandwiches = []

while sandwich_orders:

    while 'pastrami' in sandwich_orders:
        print("Sorry there is no pastrami today.")
        sandwich_orders.remove('pastrami')

    made_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(made_sandwich)
    print(f"I made you a {made_sandwich} sandwich.")


print("\nFollowing sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
