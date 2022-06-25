def login(database, username, password):
    if username in database.keys():
        if password == database[username]:
            print("\nWelcome back,", username + "!")
            return username
        else:
            print("\nIncorrect password for", username)
            return ""
    else:
        print("\nUser not found. Please register.")
        return ""


def register(database, username, password):
    if username in database.keys():
        print("Username already registered.")
        return ""
    else:
        if len(username) > 10:
            print("Username cannot be over 10 characters")
        elif len(password) < 5:
            print("Password must be at least 5 characters.")
        else:
            print(username, "has been registered.")
            return username
