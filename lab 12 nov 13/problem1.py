# Lab 12 Problem 1: Vector class
# Rubric focus: __eq__ compares two Vector objects, __add__ combines
# two vectors, and __str__ prints a readable result.


class Vector:
    def __init__(self, x, y):
        # Store the x and y components for each vector instance.
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Two vectors are equal only when both components match.
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        # Add the matching components to build a new vector.
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        # Create a readable version of the vector such as "3x + 2y".
        if self.x == 0 and self.y == 0:
            return "0"

        x_part = f"{self.x}x" if self.x != 0 else ""
        if self.y == 0:
            return x_part if x_part else "0x"

        if self.x == 0:
            return f"{self.y}y"

        sign = "+" if self.y > 0 else "-"
        return f"{self.x}x {sign} {abs(self.y)}y"


if __name__ == "__main__":
    v1 = Vector(3, 2)
    v2 = Vector(-2, 6)
    v3 = Vector(2, 0)

    # Demonstrate object comparison using __eq__.
    print("v1 == v2:", v1 == v2)
    print("v1 == Vector(3, 2):", v1 == Vector(3, 2))

    # Add vectors by combining their x and y parts.
    total = v1 + v2 + v3
    print("v1 + v2 + v3 =", total)
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)
