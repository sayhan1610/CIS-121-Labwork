# Outcome 11: Define a class with initialized dimensions, accessors, and a calculation.
class Rectangle:
    def __init__(self, width, height):
        # Store both dimensions on the rectangle instance.
        self.width = width
        self.height = height

    # Each getter reads a dimension; its setter updates that dimension.
    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def calculate_area(self):
        # A rectangle's area is its width multiplied by its height.
        return self.width * self.height


if __name__ == "__main__":
    # Create a rectangle and demonstrate its area calculation.
    rectangle = Rectangle(4, 6)
    print(rectangle.calculate_area())
