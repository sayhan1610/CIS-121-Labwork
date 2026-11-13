# Problem 7: TVShow and NetflixDashboard classes

# Part (a): TVShow class
class TVShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def preview(self):
        print(f"Previewing: {self.title} ({self.genre})")

    def __str__(self):
        return f"TVShow(title={self.title}, genre={self.genre})"


# Part (b): NetflixDashboard class
class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

    def display_recommendations(self):
        if not self.shows:
            print(f"{self.profile_name}'s dashboard is empty.")
        else:
            print(f"{self.profile_name}'s watched shows:")
            for show in self.shows:
                print(f" - {show.title} ({show.genre})")

    def __str__(self):
        return f"NetflixDashboard(profile={self.profile_name})"


# Part (c): Demonstration
if __name__ == "__main__":
    dashboard = NetflixDashboard("Sam")
    show1 = TVShow("Stranger Things", "Sci-Fi")
    show2 = TVShow("The Office", "Comedy")

    dashboard.add_show(show1)
    dashboard.add_show(show2)

    print(dashboard)
    print(show1)
    print(show2)
    dashboard.display_recommendations()
