# Outcome 11: Define a class with initialized attributes and working accessors.
class Song:
    def __init__(self, title, artist, duration_seconds):
        # Store this song's title, artist, and duration on the instance.
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    # Each getter reads an attribute; its setter updates that attribute.
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_duration_seconds(self):
        return self.duration_seconds

    def set_duration_seconds(self, duration_seconds):
        self.duration_seconds = duration_seconds


if __name__ == "__main__":
    # Create an instance and demonstrate reading its attributes.
    song = Song("Imagine", "John Lennon", 183)
    print(song.get_title(), song.get_artist(), song.get_duration_seconds())
