
def odd_sum(smaller_num, larger_num):
    if smaller_num > larger_num:
        smaller_num, larger_num = larger_num, smaller_num
    start = smaller_num if smaller_num % 2 != 0 else smaller_num + 1
    total = 0
    for value in range(start, larger_num + 1, 2):
        total += value
    return total


if __name__ == "__main__":
    start = int(input("Enter smaller number: "))
    end = int(input("Enter larger number: "))
    print(odd_sum(start, end))
