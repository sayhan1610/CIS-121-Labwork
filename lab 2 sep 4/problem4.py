# Get input for base edge and height of the triangle for a right pyramid
base_edge = float(input("Enter the base edge length of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the volume of the pyramid
volume = (base_edge ** 2 * height) / 3

# Print the volume of the pyramid
print("Volume of the pyramid:", volume)