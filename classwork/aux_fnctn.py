def add_three(x):
    y = x + 3
    return y

def sqrt(x):
    y = x ** 0.5
    return y


def find_youngest(people):
    """Return the name of the youngest person in the people dictionary."""
    if not people:
        return None
    return min(people, key=people.get)

def skip_letter(word):
    result = []
    for index, ch in enumerate(word):
        if index % 2 == 0:
            result.append(ch)
    return ''.join(result)