def city_country(city, country):
    print(f"{city.title()}, {country.title()}")


city_country('santiago', 'chile')
city_country('new york', 'united states')
city_country('brussels', 'belgium')


def make_album(artist_name, album_name):
    album = {'Artist': artist_name, 'Album': album_name}
    return album

while True:
    print("Enter 'q' to stop the program.")
    album = input("Give a name of an album: ")
    if album == 'q':
        break
    artist = input("Give name of the artist: ")
    if album == 'q':
        break

    complete_album = make_album(artist, album)
    print(complete_album)




