
def count_duplicates(num1, num2, num3):
    nums = [num1, num2, num3]
    if len(set(nums)) == 1:
        return f"You entered the same number {len(nums)} times"
    if len(set(nums)) == 2:
        return f"You entered the same number {max(nums.count(value) for value in set(nums))} times"
    return "Each number is unique"


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(count_duplicates(a, b, c))
