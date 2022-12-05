import lib2
import album 
import song

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
