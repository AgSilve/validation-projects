def main():
    password = input("Please enter new password: ")
    if is_valid_password(password):
        print("Valid password.")
    else:
        print("Invalid password.")

def is_valid_password(s):
    pass

if __name__ == "__main__":
    main()