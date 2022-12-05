import lib2
import artist
import song

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
