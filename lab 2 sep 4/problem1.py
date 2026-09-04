# Take Input for Number of Each Animal
chicken = int(input("Enter the number of chickens: "))
cows = int(input("Enter the number of cows: "))
pigs = int(input("Enter the number of pigs: "))

# Calculate Total Number of Legs
total_legs = (chicken * 2) + (cows * 4) + (pigs * 4)

# Print Total Number of Legs
print("Total number of legs:", total_legs)