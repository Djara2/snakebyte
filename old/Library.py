import file_tools as ft

class Song:
    def __init__(self, name, path, extension = None, album = None, artist = None):
        self.name = name
        self.path = path
        self.extension = extension
        self.album = album
        self.artist = artist

class Album:
    def __init__(self, name, path = None, songs = [], artist = None):
        self.name = name
        self.path = path
        self.songs = songs
        self.artist = artist

class Artist:
    def __init__(self, name, albums = []):
        self.name = name
        self.albums = albums

class Library:
    EXTENSIONS = {
            "mp3", "wav", "wma", "cda",
            "webm", "wv", "8svx", "3gp",
            "aa", "aac", "aax", "act",
            "aiff", "alac", "amr", "ape",
            "au", "awb", "dss", "dvf",
            "flac", "gsm", "iklax", "ivs",
            "m4a", "m4b", "m4p", "mmf",
            "mpc", "msv", "nmf", "ogg",
            "oga", "mogg", "opus", "ra",
            "rm", "raw", "rf64", "sln",
            "tta", "voc", "vox"}

    def __init__(self, artists = [], albums = [], songs = []):
        self.artists = artists
        self.albums = albums
        self.songs = songs
    
    def load_artists(self, start: str):
        artists = ft.get_directory_directories(start)
        for artist_name in artists:
            artist = Artist(artist_name) 
            self.artists.append(artist)

    def load_albums(self, start: str):
        if len(self.artists) != 0:
            for artist in self.artists:
                albums = ft.get_directory_directories(f"{start}\\{artist.name}")
                for album_name in albums:
                    album = Album(album_name, f"{start}\\{artist.name}\\{album_name}", [], artist)
                    songs = ft.get_directory_files(album.path)
                    for song_name in songs:
                        split_song = song_name.split(".")
                        short_name = split_song[0]
                        extension = split_song[1]
                        song = Song(short_name, f"{start}\\{artist.name}\\{album_name}\\{song_name}", extension, album, artist)
                        album.songs.append(song)
                    self.albums.append(album)

    def load_songs(self, start: str):
        for album in self.albums:
            self.songs.append(album.songs)

    def build_library(self, start: str):
        self.load_artists(start)
        self.load_albums(start)
        self.load_songs(start)

