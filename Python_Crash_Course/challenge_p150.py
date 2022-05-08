def sandwiches(*toppings):
    print(f"\nFollowing sandwich toppings are added to your sandwich:")

    for topping in toppings:
        print(f"\t{topping}")


# sandwiches('cheese', 'pepperoni', 'ham', 'butter', 'salad')
# sandwiches('cheddar', 'calabresa', 'mozzarella', 'mayo', 'salad')
# sandwiches('gouda cheese', 'pepperoni', 'ham', 'butter', 'salad')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Laurens', 'de Potter',
                             hobby='golf',
                             dream_job='machine learning engineer')


# print(user_profile)

def make_car(brand, name, **car_specs):
    car_specs['brand'] = brand
    car_specs['name'] = name
    return car_specs


car = make_car('ford', 'focus', color='dark grey', transmission='automatic')
print(car)
