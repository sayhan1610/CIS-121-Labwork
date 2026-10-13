
def find_suspect(name):
    suspects = {
        "moriarty": "Archenemy",
        "watson": "Best Friend",
        "mrs. hudson": "Landlady",
        "inspector lestrade": "Detective",
    }
    return suspects.get(name.lower(), "Unknown")


if __name__ == "__main__":
    person = input("Enter a suspect name: ")
    print(find_suspect(person))
