import lib2
import artist
import album
class Song:
    def __init__(self, name: str, album: Album, artist: Artist):
        self.name = name
        self.short_name = get_short_name(self.name)
        self.extension = get_file_extension(self.name)
        self.album = album
        self.artist = artist
        self.path = f"{music_location}\\{self.artist.name}\\{self.album.name}\\{self.name}"
