# Lab 12 Problem 4: LinearEquation class
# Rubric focus: __add__ combines two linear equations and __str__
# prints the equation in y = mx + b form.


class LinearEquation:
    def __init__(self, m, b):
        # Store the slope (m) and y-intercept (b).
        self.m = m
        self.b = b

    def __add__(self, other):
        # Adding linear equations adds their slopes and intercepts.
        if not isinstance(other, LinearEquation):
            return NotImplemented
        return LinearEquation(self.m + other.m, self.b + other.b)

    def __str__(self):
        # Display the equation as "y = mx + b".
        return f"y = {self.m}x + {self.b}"


if __name__ == "__main__":
    y1 = LinearEquation(2, 3)
    y2 = LinearEquation(-1, 5)

    # The add method combines the like terms from both equations.
    combined = y1 + y2

    print("y1:", y1)
    print("y2:", y2)
    print("y1 + y2:", combined)
