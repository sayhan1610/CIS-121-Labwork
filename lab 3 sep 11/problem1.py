'''
(a) Find four values of my var so each of the four assignment statements will be executed: each value
should cause one assignment statement to be executed.
(b) Find four ranges of my var values that will cause each of the four assignment statements to be
executed.
'''

# my_var = 5 | First value for a
# my_var = 3 | Second value for a
# my_var = 8 | Third value for a
# my_var = 12 | Fourth value for a

# my_var = all odd integers except 3 | First value for b
# my_var = 3 | Second value for b
# my_var = all even integers <= 10 | Third value for b
# my_var = All even integers > 10 | Fourth value for b

my_var = int(input("Enter an integer value: "))

if my_var % 2 == 1:
    if my_var ** 3 != 27:
        my_var = my_var + 4 # Assignment 1
        print("Assignment 1 was triggered")
    else:
        my_var /= 1.5  # Assignment 2
        print("Assignment 2 was triggered")
else:
    if my_var <= 10:
        my_var *= 2  # Assignment 3
        print("Assignment 3 was triggered")
    else:
        my_var = 2  # Assignment 4
        print("Assignment 4 was triggered")

print(my_var)

