# Problem 8: Lion and Zoo classes

# Part (a): Lion class
class Lion:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def roar(self):
        print("Roar!")

    def __str__(self):
        return f"Lion(name={self.name}, gender={self.gender})"


# Part (b): Zoo class
class Zoo:
    def __init__(self, location):
        self.location = location
        self.lions = []

    def add_lion(self, lion):
        self.lions.append(lion)

    def lions_roar(self):
        for lion in self.lions:
            lion.roar()

    def count_lions(self):
        male_count = 0
        female_count = 0

        for lion in self.lions:
            if lion.gender.lower() == "male":
                male_count += 1
            elif lion.gender.lower() == "female":
                female_count += 1

        print(f"{male_count} male, {female_count} female")

    def __str__(self):
        return f"Zoo(location={self.location})"


# Part (c): Demonstration
if __name__ == "__main__":
    zoo = Zoo("Bronx Zoo")
    lion1 = Lion("Leo", "male")
    lion2 = Lion("Luna", "female")

    zoo.add_lion(lion1)
    zoo.add_lion(lion2)

    print(zoo)
    print(lion1)
    print(lion2)
    zoo.lions_roar()
    zoo.count_lions()
