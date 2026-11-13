# Lab 12 Problem 2: Point class
# Rubric focus: __eq__ compares points, distance(other) calculates
# the distance formula, and __str__ prints a readable point.

import math


class Point:
    def __init__(self, x, y):
        # Store both coordinates of the point.
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Two points are equal only if both coordinates are identical.
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        # Use the distance formula to get the straight-line distance.
        if not isinstance(other, Point):
            raise TypeError("You must compare a Point to another Point.")
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        # Print a readable coordinate pair.
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(0, 0)
    p3 = Point(3, 4)

    # Show equality comparison with __eq__.
    print("p1 == p2:", p1 == p2)
    print("p1 == p3:", p1 == p3)

    # Calculate distance between two points using the formula.
    print("Distance between p1 and p2:", p1.distance(p2))
    print("p1:", p1)
    print("p2:", p2)
