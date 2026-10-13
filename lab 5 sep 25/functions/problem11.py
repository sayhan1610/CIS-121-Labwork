
def find_relation(name):
    relations = {
        "darth vader": "Father",
        "leia": "Sister",
        "han": "Brother in law",
        "r2d2": "Droid",
    }
    return relations.get(name.lower(), "Unknown")


if __name__ == "__main__":
    person = input("Enter a person: ")
    print(find_relation(person))
