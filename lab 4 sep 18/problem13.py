height = int(input("Enter the triangle height: "))

# Each row contains one more asterisk than the previous row
for i in range(1, height + 1):
    print("*" * i)