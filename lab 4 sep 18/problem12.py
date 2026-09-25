# Ask the user for two integer, and then build a multiplication table based on those numbers. So basically if a user selects 8 and 7, you out put a 8x7 multiplication grid.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number "))

for row in range(1, number1 + 1): # get number of of rows and arrange them
    for column in range(1, number2 + 1): # get number of columns and arrange them
        print(row * column, end="\t") # prints a table from row and column 
    print() # blanks space of cleanliness