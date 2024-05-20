def main():
    password = input("Please enter new password: ")
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
    pass

def has_uppercase(password):
    pass

def has_lowercase(password):
    pass

def has_digit(password):
    pass

def has_special_character(password):
    pass

def no_spaces(password):
    pass


if __name__ == "__main__":
    main()