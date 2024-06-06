import re

def main():
    email = input('Enter your email address: ')
    if is_valid_email(email):
        print('Valid email.')
    else:
        print('Invalid email.')

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9\.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    main()