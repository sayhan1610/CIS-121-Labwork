
def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "equilateral"
    if side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    return "scalene"


if __name__ == "__main__":
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    print(triangle_type(a, b, c))
