
def city_country(city, country, population=''):
    """Generate a text with the city and country"""
    if population:
        full = f"{city}, {country} - {population}"
        return full.title()
    else:
        full = f"{city}, {country}"
        return full.title()


print(city_country('brugge', 'belgium', 300_000))