large = int(input("Enter a larger integer: "))
small = int(input("Enter a small integer "))

count = 0

while large > small:
    large = large / 2
    count += 1
    # print(f"Halved {count} times. Current number is {large}.")
    
print(f"You can halve it {count} times")