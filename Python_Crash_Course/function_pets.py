def describe_pet(animal_type='walrus', pet_name='cat'):
    """Display information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('cat', 'zorro')
describe_pet(pet_name='benji', animal_type='dog')
describe_pet(pet_name='loui')
