# ask user user for three numbers
num1 = int(input("Pick a number: "))
num2 = int(input("Pick another number: "))
num3 = int(input("Pick another number: "))

# determine the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# output the result
print(f"The smallest number is {smallest}.")