def main():
    username = input("Enter username: ")
    if is_valid_username(username):
        print("Valid username.")
    else:
        print("Invalid username.")

def is_valid_username(username):
    return(
        starts_with_letter(username) and
        check_length(username) and
        not_ends_with_underscore(username) and
        contain_valid_characters(username)
    )

def starts_with_letter(username):
    pass

def check_length(username):
    pass

def not_ends_with_underscore(username):
    pass

def contain_valid_characters(username):
    pass

if __name__ == "__main__":
    main()