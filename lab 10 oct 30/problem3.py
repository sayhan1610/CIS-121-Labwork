# Outcome 11: Define a class with initialized attributes and working accessors.
class Movie:
    def __init__(self, title, director, runtime_minutes):
        # Store this movie's title, director, and runtime on the instance.
        self.title = title
        self.director = director
        self.runtime_minutes = runtime_minutes

    # Each getter reads an attribute; its setter updates that attribute.
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_director(self):
        return self.director

    def set_director(self, director):
        self.director = director

    def get_runtime_minutes(self):
        return self.runtime_minutes

    def set_runtime_minutes(self, runtime_minutes):
        self.runtime_minutes = runtime_minutes


if __name__ == "__main__":
    # Create an instance and demonstrate reading its attributes.
    movie = Movie("Hidden Figures", "Theodore Melfi", 127)
    print(movie.get_title(), movie.get_director(), movie.get_runtime_minutes())
