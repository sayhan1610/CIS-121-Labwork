number = int(input("Enter an integer: "))
total = 0

# Square each integer from 1 through number
for i in range(1, number + 1):
    total += i ** 2

print(total)