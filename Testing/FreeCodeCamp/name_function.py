
# This will be used as an example for unittests.
def formatted_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
