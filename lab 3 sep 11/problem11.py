# ask the user for three integers
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

# sort the numbers using conditional comparisons and swaps
if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp
if num2 < num3:
    temp = num2
    num2 = num3
    num3 = temp
if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp
    
# Display the sorted integers
print(f"The integers in decreasing order are: {num1}, {num2}, {num3}")