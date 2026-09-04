# Take Input for Height and Widths of the Trapezoid
height = float(input("Enter the height of the trapezoid: "))
width_a = float(input("Enter the width A of the trapezoid: "))
width_b = float(input("Enter the width B of the trapezoid: "))

# Calculate Area of the Trapezoid
area = (height * (width_a + width_b)) / 2

# Print Area of the Trapezoid
print("Area of the trapezoid:", area)
