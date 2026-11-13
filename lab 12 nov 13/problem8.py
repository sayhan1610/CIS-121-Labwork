# Lab 12 Problem 8: Rectangle class
# Rubric focus: __mul__ modifies the current rectangle by an integer,
# area() calculates the area, and __str__ prints dimensions clearly.


class Rectangle:
    def __init__(self, width, height):
        # Store the width and height of the rectangle.
        self.width = width
        self.height = height

    def area(self):
        # Area is width times height.
        return self.width * self.height

    def __mul__(self, factor):
        # Multiply both dimensions by the same integer, modifying this object.
        if not isinstance(factor, int):
            return NotImplemented
        self.width *= factor
        self.height *= factor
        return self

    def __str__(self):
        # Print dimensions in a readable format.
        return f"Rectangle({self.width} x {self.height})"


if __name__ == "__main__":
    r1 = Rectangle(4, 5)

    # The current rectangle is modified in place when multiplied.
    r1 * 3

    print("Rectangle area:", r1.area())
    print("Result:", r1)
