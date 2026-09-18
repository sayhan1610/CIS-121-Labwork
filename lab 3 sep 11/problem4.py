# ask user for three numbers
num1 = int(input("Pick a number: "))
num2 = int(input("Pick another number: "))
num3 = int(input("Pick another number: "))

# determine the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# output the result
print(f"The largest number is {largest}.")