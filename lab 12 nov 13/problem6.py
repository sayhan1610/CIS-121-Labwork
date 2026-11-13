# Lab 12 Problem 6: RGBColor class
# Rubric focus: __add__ averages matching color channels and __str__
# prints the RGB values in a readable format.


class RGBColor:
    def __init__(self, r, g, b):
        # Each channel must stay between 0 and 255.
        self.r = max(0, min(255, r))
        self.g = max(0, min(255, g))
        self.b = max(0, min(255, b))

    def __add__(self, other):
        # Adding two colors uses the average of each channel.
        if not isinstance(other, RGBColor):
            return NotImplemented

        new_r = int(round((self.r + other.r) / 2))
        new_g = int(round((self.g + other.g) / 2))
        new_b = int(round((self.b + other.b) / 2))
        return RGBColor(new_r, new_g, new_b)

    def __str__(self):
        # Show the color in the format RGB(red, green, blue).
        return f"RGB({self.r}, {self.g}, {self.b})"


if __name__ == "__main__":
    c1 = RGBColor(170, 150, 200)
    c2 = RGBColor(30, 100, 60)
    c3 = RGBColor(80, 200, 140)

    # Combine colors by chaining __add__, which averages each channel.
    combined = c1 + c2 + c3

    print("c1:", c1)
    print("c2:", c2)
    print("c3:", c3)
    print("c1 + c2 + c3:", combined)
