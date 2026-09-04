import math

# Take input for the radius and height of the cone
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

# Calculate the volume of the cone
volume = (math.pi * (radius ** 2) * height) / 3

# Print the volume of the cone
print("Volume of the cone:", volume)