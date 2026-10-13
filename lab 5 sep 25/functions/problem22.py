
import math


def cone_volume(r, h):
    return math.pi * (r ** 2) * h / 3


if __name__ == "__main__":
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    print(cone_volume(radius, height))
