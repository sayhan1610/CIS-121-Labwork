
def get_drink_id(flavor, capacity):
    return flavor[:3] + str(capacity)


if __name__ == "__main__":
    flavor = input("Enter a flavor: ")
    size = int(input("Enter the capacity: "))
    print(get_drink_id(flavor, size))
