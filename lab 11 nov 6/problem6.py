# Problem 6: Song and Playlist classes

# Part (a): Song class
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def play(self):
        print(f"Playing: {self.title} by {self.artist}")

    def __str__(self):
        return f"Song(title={self.title}, artist={self.artist})"


# Part (b): Playlist class
class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        for song in self.songs:
            song.play()

    def __str__(self):
        return f"Playlist(name={self.playlist_name})"


# Part (c): Demonstration
if __name__ == "__main__":
    playlist = Playlist("Study Mix")
    song1 = Song("Midnight City", "M83")
    song2 = Song("Dreams", "Fleetwood Mac")

    playlist.add_song(song1)
    playlist.add_song(song2)

    print(playlist)
    print(song1)
    print(song2)
    playlist.play_all()
