def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"hello, {name.title()}!"
        print(msg)


user_names = ['june', 'tom', 'marco', 'luiz']
greet_users(user_names)