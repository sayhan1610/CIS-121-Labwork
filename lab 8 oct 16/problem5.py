"""Look up Luke Skywalker's relationship to a person."""


def find_relation(name=""):
    """Return the known relationship, or 'Unknown' for other names."""
    relations = {
        "darth vader": "Father",
        "leia": "Sister",
        "han": "Brother in law",
        "r2d2": "Droid",
    }
    return relations.get(name.strip().casefold(), "Unknown")


if __name__ == "__main__":
    print(find_relation("Darth Vader"))
    print(find_relation("R2D2"))
    print(find_relation("Jabba the Hutt"))
    print(find_relation())
