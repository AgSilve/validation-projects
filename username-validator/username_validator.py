import re

def main():
    username = input("Enter username: ")
    if is_valid_username(username):
        print("Valid username.")
    else:
        print("Invalid username.")

def is_valid_username(username):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{1,14}$"
    return bool(re.match(pattern, username) and not username.endswith("_"))

if __name__ == "__main__":
    main()