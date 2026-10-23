# Problem 3: Return every even number between two integers (inclusive).

def even(smaller_num, larger_num):
    """Return all even numbers from smaller_num to larger_num."""
    start, end = sorted((smaller_num, larger_num))
    if start % 2 != 0:
        start += 1
    return list(range(start, end + 1, 2))


if __name__ == "__main__":
    print(even(37, 1050))
    print(even(1, 2000))
    print(even(50, 199))
    
    
    
    
    
def output_even(smaller_num, larger_num):
    result = []
    for i in range(smaller_num, larger_num + 1):
        if i % 2 == 0:
            result.append(i)
    return result