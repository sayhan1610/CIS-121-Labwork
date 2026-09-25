total = 0

# makes a continuous loop
while True:
    num = int(input("Enter an integer: ")) # takes an input

    if num < 0:
        break # stops if negative

    total += num # sums the listed numbers

print("Sum:", total) # outputs the sum