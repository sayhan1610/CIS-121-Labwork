from math import pi


# Outcome 11: Define a class with an initialized radius, accessors, and a calculation.
class Circle:
    def __init__(self, radius):
        # Store the circle's radius on the instance.
        self.radius = radius

    # The getter reads the radius; the setter updates it.
    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        # A circle's circumference is two times pi times its radius.
        return 2 * pi * self.radius


if __name__ == "__main__":
    # Create a circle and demonstrate its circumference calculation.
    circle = Circle(5)
    print(circle.calculate_circumference())
