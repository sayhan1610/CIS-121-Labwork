
def total_score(two_pointers, three_pointers):
    return two_pointers * 2 + three_pointers * 3


if __name__ == "__main__":
    two = int(input("Enter two-pointers: "))
    three = int(input("Enter three-pointers: "))
    print(total_score(two, three))
