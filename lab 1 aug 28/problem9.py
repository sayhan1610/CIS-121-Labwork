'''x = 3 #takes the value 3 and assigns it to the variable x
y = 7 #takes the value 7 and assigns it to the variable y

temp_1 = x #takes the value of x and assigns it to the variable temp_1
temp_2 = y #takes the value of y and assigns it to the variable temp_2

x = temp_2 #takes the value of temp_2 and assigns it to the variable x
y = temp_1 #takes the value of temp_1 and assigns it to the variable y

print(f"x: {x}, y: {y}") #outputs a message in the format of "x: x, y: y."

'''

# Set the two values that will be swapped.
x=3
y=7

# Store each value temporarily before switching their positions.
temp_a = x
temp_b = y

# Swap the values and display the result.
x = temp_b
y = temp_a

print(f"x = {x} and y = {y}")