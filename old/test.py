import lib2

library = lib2.Library()

while True:
    action = input("> ")
    if action == "artists":
        x = 0
        for artist in library.artists:
            print(f"{x}. {artist.name}")

    if action == "albums":
        x = 0
        for album in library.albums:
            print(f"{x}. {album.name} ({album.path})")

    if action == "songs":
        x = 0
        for song in library.songs:
            print(f"{x}. {song.name} ({song.path})")

    if action == "library":
        for artist in library.artists:
            print(f"{artist.name}")
            for album in artist.albums:
                print(f"\t- {album.name}")
                for song in album.songs:
                    print("\t\t{song.name}") 
            print()
