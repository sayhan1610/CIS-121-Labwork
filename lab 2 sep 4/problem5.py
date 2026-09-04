import math

# Take input for for height and radius of the cylinder
height = float(input("Enter the height of the cylinder: "))
radius = float(input("Enter the radius of the cylinder: "))

# Calculate the volume of the cylinder
volume = math.pi * (radius ** 2) * height

# Print the volume of the cylinder
print("Volume of the cylinder:", volume)