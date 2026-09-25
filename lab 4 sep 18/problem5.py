number = int(input("Enter an integer: "))

# Check every number from 1 through the input
for i in range(1, number + 1):
    if number % i == 0:
        print(i)