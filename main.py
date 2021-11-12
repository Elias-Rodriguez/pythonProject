# TODO: Import Artist from Artist.py and Artwork from Artwork.py
from Artist import Artist
from Artwork import Artwork

if __name__ == "__main__":
    user_artist_name = input("Type in Artist Name:")
    user_birth_year = int(input("Type in the artist's birth year:"))
    user_death_year = int(input("Type in the artist's death year or -1 if still alive:"))
    user_title = input("Type in the title:")
    user_year_created = int(input("Type in the year it was created:"))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()
