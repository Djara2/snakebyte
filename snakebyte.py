import file_tools as ft
import display_tools as dt
import os_tools as ot
import safety
import os
import graphics 
from rich.console import Console

class Song:
    def __init__(self, name, artist, album):
        self.name = name
        self.artist = artist
        self.album = album

class Album:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

def get_music_location():
    config_file = open("config.txt", "r")
    config_file_contents = config_file.read()
    music_location = config_file_contents.split('\n')[0].split(" = ")[1]
    config_file.close()
    return music_location

def get_file_extension(file_name: str) -> str:
    list_form = file_name.split(".")
    extension = list_form[len(list_form)-1]
    return extension

def get_short_name(file_name: str) -> str:
    list_form = file_name.split(".")
    short_name = list_form[0]
    return short_name

music_location = get_music_location()
OPERATING_SYSTEM = ot.get_os()
console = Console()

def get_artists():
    artists = ft.get_directory_directories(music_location)
    return artists
   
def get_albums(artist: str):
    if ot.get_os == "Windows":
        albums = ft.get_directory_directories(f"{music_location}\\{artist}")
    else:
        albums = ft.get_directory_directories(f"{music_location}/{artist}")
    album_instances = []
    for album_title in albums:
        album = Album(album_title, artist)
        album_instances.append(album)
    return album_instances
   
def get_songs(artist: str, album: str):
    if ot.get_os == "Windows":
        files = ft.get_directory_files(f"{music_location}\\{artist}\\{album.name}")
    else:
        files = ft.get_directory_files(f"{music_location}/{artist}/{album.name}")
    songs = []
    for file in files:
        extension = get_file_extension(file)
        if extension in EXTENSIONS:
            song_instance = Song(file, artist, album)
            songs.append(song_instance)
    return songs
           
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

def build_library():
    library = dict()
    artists = get_artists()
    for artist in artists:
        albums = get_albums(artist)
        library[artist] = dict()
        for album in albums:
            songs = get_songs(artist, album)
            library[artist][album] = songs
    return library
 
def print_library(library: dict):
    for artist in library.keys():
        print(artist)
        for album in library[artist].keys():
            print(f"\t{album}")
            print(f"\t{'━' * len(album)}")
            for song in library[artist][album]:
                print(f"\t{song.name}")
            print()
        print()
    print()

def get_all_artists(library: dict):
    return list(library.keys())
 
def get_all_albums(library: dict):
    albums = []
    for artist in library.keys():
        for album in library[artist].keys():
            albums.append(album)
    return albums

def get_all_album_names(albums: list):
    album_names = []
    for album in albums:
        album_names.append(album.name)
    return album_names

def get_all_songs(library: dict):
    songs = []
    for artist in library.keys():
        for album in library[artist].keys():
            for song in library[artist][album]:
                songs.append(song)
    return songs

def enumerate_list(array, start = 0, print_numbers = True):
    if print_numbers:
        upper = len(array) - 1
        len_upper = len(str(upper))
        for item in array:
            len_start = len(str(start))
            difference = len_upper - len_start
            if type(item) in [type(Song(None, None, None)), type(Album(None, None))]:
                print(f"{'0' * difference}{start}. {item.name}")
            else:
                print(f"{'0' * difference}{start}. {item}")
                
            start += 1
    else:
        for item in array:
            if type(item) in [type(Song(None, None, None)), type(Album(None, None))]:
                print(item.name)
            else:
                print(item)

def show_mpv_controls():
    ot.clear()
    terminal_columns = dt.get_terminal_columns()
    right_padding = terminal_columns - len(" Player")
    console.print(f"[{graphics.MENU_HEADER_SCHEME}] Player{' ' * right_padding}[/]")
    print()
    buffer = " " * 4
    console.print(f"[u][bold #ff7200]Pause[/][/]{buffer}[u][bold #ff7200]Quit[/][/]")
    console.print(f"P{' ' * (len('Pause') + len(buffer) - 1)}Q")
    print()

def play_song(song: Song):
    show_mpv_controls()
    if OPERATING_SYSTEM == "Windows":
        cmd = f"mpv --no-audio-display \"{music_location}\\{song.artist}\\{song.album.name}\\{song.name}\""
    else:
        cmd = f"mpv --no-audio-display \"{music_location}/{song.artist}/{song.album.name}/{song.name}\""
    os.system(cmd)

def play_album(album: Album):
    show_mpv_controls()
    if OPERATING_SYSTEM == "Windows":
        cmd = f"mpv --no-audio-display \"{music_location}\\{album.artist}\\{album.name}\""
    else:
        cmd = f"mpv --no-audio-display \"{music_location}/{album.artist}/{album.name}\""
    os.system(cmd)

def title_print(title: str):
    print(title)
    print("━" * len(title))

def sentence_case(text):
    text = text.split()
    new_text = ""
    x = 0
    for word in text:
        new_text += word[0].upper()
        new_text += word[1:]
        if x < len(text)-1:
            new_text += " "
        x += 1
    return new_text
    

library = build_library()
artists = get_all_artists(library)
albums = get_all_albums(library)
album_names = get_all_album_names(albums)
songs = get_all_songs(library)
MAIN_TEXT = [
    "SnakeByte",
    "A Free and Open Source command-line music player.",
    "Powered by mpv"
    "",
    "",
    "[cyan]Know what you want?[/]",
    "━" * len('Know what you want?'),
    "Enter the name of an artist to jump straight to their discograpy",
    "You can also enter the name of an album to jump straight to it",
    "", 
    "[cyan]Don't know what you want?[/]",
    "━" * len('Don\'t know what you want?'),
    "Enter \"artists\" to see all artists",
    "Enter \"albums\" to see all albums",
    "Enter \"songs\" to see all songs",
]
focus = None

while True:
    ot.clear()
    
    if focus == None:
        left_padding = graphics.center_print(MAIN_TEXT)
    else:
        if type(focus) == type("str"): #case where the focus is an artist, as all the other things are represented as objects.
            ARTIST_TEXT = [
            f"{focus} [white]albums[/]"
            ]
            x = 1
            str_len_albums = len(str(len(albums)))
            for album in library[focus].keys():
                difference = str_len_albums - len(str(x))
                ARTIST_TEXT.append(f"{'0' * difference}{x}. {album.name}")
                x += 1
            left_padding = graphics.center_print(ARTIST_TEXT)
            
        elif type(focus) == type(Album(None, None)):
            ALBUM_TEXT = [
            f"{focus.name}[white] by {focus.artist}[/]"
            ]
            for song in library[focus.artist][focus]:
                ALBUM_TEXT.append(song.name)
            left_padding = graphics.center_print(ALBUM_TEXT)
            
    if focus == None:
        print("\n\n\n")

    else:
        print()
    
    print(f"{' ' * left_padding}", end = "")
    action = graphics.prompt(" Command ")
    
    if action == "exit":
        exit()
    
    if focus != None:
        if safety.try_str_to_int(action):
            action = int(action) - 1
            
            if type(focus) == type("str"):
                if safety.index_in_bounds(action, library[focus].keys()):
                    focus = list(library[focus].keys())[action]
            
            elif type(focus) == type(Album(None, None)):
                if safety.index_in_bounds(action, library[focus.artist][focus]):
                    play_song(library[focus.artist][focus][action])
        
        elif action in ["b", "back"]:
            if type(focus) == type("str"):
                focus = None
            elif type(focus) == type(Album(None, None)):
                focus = focus.artist
        
        elif action == "all":
            if type(focus) == type(Album(None, None)):
                play_album(focus)
    
    elif (action in artists):
        focus = action
    
    elif (sentence_case(action) in artists):
        focus = sentence_case(action)
    
    elif (action in album_names) or (sentence_case(action) in album_names):
        if (not action in artists) or (not sentence_case(action) in artists):
            try:
                focus = albums[album_names.index(action)]
            except:
                focus = albums[album_names.index(sentence_case(action))]
    
    elif action == "artists":
        ot.clear()
        ALL_ARTISTS_TEXT = ["Artists in Your Library"]
        x = 1
        str_len_artists = len(str(len(artists)))
        for artist in artists:
            difference = str_len_artists - len(str(x))
            ALL_ARTISTS_TEXT.append(f"{'0' * difference}{x}. {artist}")
            x += 1
        left_padding = graphics.center_print(ALL_ARTISTS_TEXT)
        print(f"\n{' ' * left_padding}", end = "")
        action = graphics.prompt(" Explore one of these artists? ")
        
        if safety.try_str_to_int(action):
            action = int(action)-1
            if safety.index_in_bounds(action, artists):
                focus = artists[action]
                
    elif action == "albums":
        ot.clear()
        ALL_ALBUMS_TEXT = ["Albums in Your Library"]
        x = 1
        str_len_albums = len(str(len(albums)))
        for album in albums:
            difference = str_len_albums - len(str(x))
            ALL_ALBUMS_TEXT.append(f"{'0' * difference}{x}. {album.name}")
            x += 1
        left_padding = graphics.center_print(ALL_ALBUMS_TEXT)
        print(f"\n{' ' * left_padding}", end = "")
        action = graphics.prompt(" Play any of these albums? ")
        
        if safety.try_str_to_int(action):
            action = int(action) - 1
            if safety.index_in_bounds(action, albums):
                play_album(albums[action])
          
    elif action == "songs":
        ot.clear()
        ALL_SONGS_TEXT = ["Songs in Your Library"]
        x = 1
        str_len_songs = len(str(len(songs)))
        for song in songs:
            difference = str_len_songs - len(str(x))
            ALL_SONGS_TEXT.append(f"{'0' * difference}{x}. {song.name}")
            x += 1
        left_padding = graphics.center_print(ALL_SONGS_TEXT)
        print(f"\n{' ' * left_padding}", end = "")
        action = graphics.prompt(" Play any of these songs? ")
        if safety.try_str_to_int(action):
            action = int(action)-1
            if safety.index_in_bounds(action, songs):
               play_song(songs[action])        
    else:
        print("Unrecognized input")