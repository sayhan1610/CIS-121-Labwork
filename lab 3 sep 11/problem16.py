side_1 = float(input("pick side length 1: "))
side_2 = float(input("pick side length 2: "))
side_3 = float(input("pick side length 3: "))

# Classify the triangle by comparing its side lengths.
if side_1 == side_2 == side_3:
    print("equilateral triangle")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("isosceles triangle")
else:
    print("scalene triangle")