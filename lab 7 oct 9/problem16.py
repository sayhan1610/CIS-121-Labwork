# Problem 16: Return a list of just the student names from a dictionary.

def get_names(names_of_tech_ids):
    """Return the dictionary values as a list."""
    return list(names_of_tech_ids.values())


if __name__ == "__main__":
    print(get_names({"01475": "Steve", "87469": "Alice", "654123": "Bob"}))
    print(get_names({"ID1": "John", "ID2": "Emma", "ID3": "Liam"}))
    print(get_names({}))
