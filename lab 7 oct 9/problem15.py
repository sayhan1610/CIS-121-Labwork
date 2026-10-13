# Problem 15: Return the majority element in a list of integers.

def majority_element(nums):
    """Return the number that appears more than half the time."""
    counts = {}
    for number in nums:
        counts[number] = counts.get(number, 0) + 1
    half = len(nums) / 2
    for number, count in counts.items():
        if count > half:
            return number
    return None


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element([2, 2, 3, 2, 1, 2, 1, 4, 4, 1, 2, 2]))
