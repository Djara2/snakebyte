import file_tools as ft
import artist
import album
import song

def get_music_location():
    config_file = open("config.txt", "r")
    config_file_contents = config_file.read()
    music_location = config_file_contents.split('\n')[0].split(" = ")[1]
    config_file.close()
    return music_location

def get_file_extension(file_name: str) -> str:
    list_form = file_name.split(".")
    extension = list_form[1]
    return extension

def get_short_name(file_name: str) -> str:
    list_form = file_name.split(".")
    short_name = list_form[0]
    return short_name

music_location = get_music_location()

EXTENSIONS = { "mp3", "wav", "wma", "cda",
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

class Song:
    def __init__(self, name: str, album: Album, artist: Artist):
        self.name = name
        self.short_name = get_short_name(self.name)
        self.extension = get_file_extension(self.name)
        self.album = album
        self.artist = artist
        self.path = f"{music_location}\\{self.artist.name}\\{self.album.name}\\{self.name}"


class Album:
    def __init__(self, name: str, artist: Artist):
        self.name = name
        self.artist = artist
        self.path = f"{music_location}\\{self.artist.name}\\{self.name}"
        self.songs = []
        song_files = ft.get_directory_files(self.path)
        for song_name in song_files:
            extension = get_file_extension(song_name)
            if extension in EXTENSIONS:
                song = Song(song_name, self, self.artist)
                self.songs.append(song)

class Artist:
    def __init__(self, name: str):
        self.name = name
        self.path = f"{music_location}\\{self.name}"
        self.albums = []
        self.songs = []
        album_folders = ft.get_directory_directories(self.path)
        for album_name in album_folders:
            album = Album(album_name, self)
            self.albums.append(album)
        
        for album in self.albums:
            for song in album.songs:
                self.songs.append(song)

class Library:
    def __init__(self):
        root_contents = ft.get_directory_directories(music_location)
        self.artists = []
        self.albums = []
        self.songs = []
        for directory in root_contents:
            artist = Artist(directory)
            self.artists.append(Artist)

        for artist in self.artists:
            for album in artist.albums:
                self.albums.append(album)

        for album in self.albums:
            for song in album.songs:
                self.songs.append(song)


