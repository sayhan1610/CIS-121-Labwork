# Lab 12 Problem 9: Playlist class
# Rubric focus: __add__ combines two playlists and __str__ prints the
# song list in a readable way.


class Playlist:
    def __init__(self, name="New Playlist", songs=None):
        # Default playlist name is required; songs is optional.
        self.name = name
        self.songs = [] if songs is None else list(songs)

    def add_song(self, song_title):
        # Add a title to the list of songs in the playlist.
        self.songs.append(song_title)

    def __add__(self, other):
        # Combine two playlists by appending the songs from the second list.
        if not isinstance(other, Playlist):
            return NotImplemented

        combined_name = f"{self.name} + {other.name}"
        combined_songs = self.songs + other.songs
        return Playlist(combined_name, combined_songs)

    def __str__(self):
        # Print the playlist name and each song in the list.
        song_list = ", ".join(self.songs)
        return f"{self.name}: [{song_list}]"


if __name__ == "__main__":
    p1 = Playlist("Favorites", ["Song A", "Song B"])
    p2 = Playlist("Road Trip", ["Song C", "Song D"])

    combined = p1 + p2

    print("p1:", p1)
    print("p2:", p2)
    print("p1 + p2:", combined)
