# Problem 3: Droid and Starship classes

# Part (a): Droid class
class Droid:
    def __init__(self, designation, series):
        self.designation = designation
        self.series = series

    def get_series(self):
        return self.series

    def set_series(self, series):
        self.series = series

    def communicate(self):
        print("Beep-Bloop-Blop!")

    def __str__(self):
        return f"Droid(designation={self.designation}, series={self.series})"


# Part (b): Starship class
class Starship:
    def __init__(self, name):
        self.name = name
        self.droids = []

    def add_droid(self, droid):
        self.droids.append(droid)

    def droids_communicate(self):
        for droid in self.droids:
            droid.communicate()

    def __str__(self):
        return f"Starship(name={self.name})"


# Part (c): Demonstration
if __name__ == "__main__":
    starship = Starship("Voyager")
    droid1 = Droid("R2-D2", "Astromech")
    droid2 = Droid("BB-8", "Scout")

    starship.add_droid(droid1)
    starship.add_droid(droid2)

    print(starship)
    print(droid1)
    print(droid2)
    starship.droids_communicate()
