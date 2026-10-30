# Outcome 11: Define a class with initialized color channels, accessors, and a calculation.
class ColorRGB:
    def __init__(self, red, green, blue):
        # Store the red, green, and blue channel values on the instance.
        self.red = red
        self.green = green
        self.blue = blue

    # Each getter reads a channel; its setter updates that channel.
    def get_red(self):
        return self.red

    def set_red(self, red):
        self.red = red

    def get_green(self):
        return self.green

    def set_green(self, green):
        self.green = green

    def get_blue(self):
        return self.blue

    def set_blue(self, blue):
        self.blue = blue

    def to_grayscale(self):
        # Weight the channels using the assignment's grayscale formula.
        return 0.3 * self.red + 0.59 * self.green + 0.11 * self.blue


if __name__ == "__main__":
    # Create a color and demonstrate its grayscale calculation.
    color = ColorRGB(100, 150, 200)
    print(color.to_grayscale())
