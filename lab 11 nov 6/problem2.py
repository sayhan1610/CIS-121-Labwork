# Problem 2: Duck and Pond classes

# Part (a): Duck class
class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def speak(self):
        print("Quack!")

    def __str__(self):
        return f"Duck(name={self.name}, color={self.color})"


# Part (b): Pond class
class Pond:
    def __init__(self, name):
        self.name = name
        self.ducks = []

    def add_duck(self, duck):
        self.ducks.append(duck)

    def ducks_quack(self):
        for duck in self.ducks:
            duck.speak()

    def __str__(self):
        return f"Pond(name={self.name})"


# Part (c): Demonstration
if __name__ == "__main__":
    pond = Pond("Sunny Pond")
    duck1 = Duck("Daffy", "yellow")
    duck2 = Duck("Poppy", "white")

    pond.add_duck(duck1)
    pond.add_duck(duck2)

    print(pond)
    print(duck1)
    print(duck2)
    pond.ducks_quack()
