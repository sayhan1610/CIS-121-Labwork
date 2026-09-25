largest_even = -1

# Keep reading numbers until a negative number is entered
while True:
    number = int(input("Enter an integer: "))

    if number < 0:
        break

    # Update the largest even number if necessary
    if number % 2 == 0 and number > largest_even:
        largest_even = number

print(largest_even)