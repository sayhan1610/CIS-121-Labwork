
def output_even(smaller_num, larger_num):
    if smaller_num > larger_num:
        smaller_num, larger_num = larger_num, smaller_num
    return list(range(smaller_num if smaller_num % 2 == 0 else smaller_num + 1, larger_num + 1, 2))


if __name__ == "__main__":
    start = int(input("Enter smaller number: "))
    end = int(input("Enter larger number: "))
    print(output_even(start, end))
