# Take Input for Number of Each Type of Shot
two_pointers = int(input("Enter the number of two-pointers made: "))
three_pointers = int(input("Enter the number of three-pointers made: "))

# Calculate Total Points
total_points = (two_pointers * 2) + (three_pointers * 3)

# Print Total Points
print("Total points scored:", total_points)