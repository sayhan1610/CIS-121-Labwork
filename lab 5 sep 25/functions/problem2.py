
def access_rights(role):
    role = role.lower()
    rights = {
        "admin": "full",
        "user": "limited",
        "guest": "view",
    }
    return rights.get(role, "unknown")


if __name__ == "__main__":
    role = input("Enter a role: ")
    print(access_rights(role))
