from math import sqrt


# Outcome 11: Define a class with initialized components, accessors, and a calculation.
class Vector:
    def __init__(self, x_direction, y_direction):
        # Store the vector's two components on the instance.
        self.x_direction = x_direction
        self.y_direction = y_direction

    # Each getter reads a component; its setter updates that component.
    def get_x_direction(self):
        return self.x_direction

    def set_x_direction(self, x_direction):
        self.x_direction = x_direction

    def get_y_direction(self):
        return self.y_direction

    def set_y_direction(self, y_direction):
        self.y_direction = y_direction

    def get_magnitude(self):
        # Use the Pythagorean theorem to find the vector's magnitude.
        return sqrt(self.x_direction**2 + self.y_direction**2)


if __name__ == "__main__":
    # Create a vector and demonstrate its magnitude calculation.
    vector = Vector(3, 4)
    print(vector.get_magnitude())
