# Outcome 11: Define a class with initialized coordinates, accessors, and an action.
class Point:
    def __init__(self, x_coordinate, y_coordinate):
        # Store both coordinates on this Point instance.
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # Each getter reads a coordinate; its setter updates that coordinate.
    def get_x_coordinate(self):
        return self.x_coordinate

    def set_x_coordinate(self, x_coordinate):
        self.x_coordinate = x_coordinate

    def get_y_coordinate(self):
        return self.y_coordinate

    def set_y_coordinate(self, y_coordinate):
        self.y_coordinate = y_coordinate

    def print_info(self):
        # Include the spaces and labels from the requested point format.
        print(f"(x,y)=( {self.x_coordinate}, {self.y_coordinate} )")


if __name__ == "__main__":
    # Create a point and call its required display method.
    point = Point(4, 5)
    point.print_info()
