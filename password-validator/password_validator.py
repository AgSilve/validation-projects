def main():
    password = input("Enter password: ")
    if is_valid_password(password):
        print("Valid password.")
    else:
        print("Invalid password.")

def is_valid_password(password):
    return(
        check_length(password) and
        has_uppercase(password) and
        has_lowercase(password) and
        has_digit(password) and
        has_special_character(password) and
        no_spaces(password)

    )

def check_length(password):
    return len(password) >= 8

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_character(password):
    special_characters = [',', '.', '?', '/', '!', '@', '#', '$', '%', '^', '&', '(', ')']
    return any(char in special_characters for char in password)

def no_spaces(password):
    return " " not in password


if __name__ == "__main__":
    main()