
import math


def pyramid_volume(b, h):
    return (b ** 2 * h) / 3


if __name__ == "__main__":
    base = float(input("Enter base edge: "))
    height = float(input("Enter height: "))
    print(pyramid_volume(base, height))
