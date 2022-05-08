def make_shirt(size='large', text='I love python'):
    print(f"The size of your shirt will be {size}, and have the text '{text}' written on it.")


make_shirt('medium', 'hello world!')


def describe_city(city, country="fairyland"):
    print(f"{city} is in {country}.")


describe_city('brugge')
describe_city('sao paulo', 'brazil')
describe_city('berlin', 'germany')