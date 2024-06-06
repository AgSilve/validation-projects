# Username Validator

## Overview

The Username Validator script checks whether a given username meets specific criteria and determines its validity.

## Features

The Username Validator script validates usernames based on the following criteria:

- Must start with a letter.
- Can contain letters (both uppercase and lowercase), digits, and underscores (_).
- Length should be between 3 and 15 characters.
- Should not end with an underscore.

## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/AgSilve/validation-projects.git
   ```

2. Navigate to the project directory:
   ```bash
   cd username-validator
   ```

3. Run the script:
   ```bash
   python3 username_validator.py
   ```

4. Enter a username when prompted.

## Implementation Details

The script consists of two main functions:
- `main()`:Prompts the user to enter a username and calls the `is_valid_username()` function to validate it.
- `is_valid_username(username)`: Validates the username against the defined criteria using a regular expression pattern.

## Regular Expression Pattern

The regular expression pattern used for username validation is as follows:
```python
pattern = r"^[a-zA-Z][a-zA-Z0-9_]{1,14}$"
```
This pattern ensures that the username starts with a letter, followed by any combination of letters, digits, or underscores, with a length between 3 and 15 characters.

## Example

```
$ python3 username_validator.py
Enter username: AgSpades
Valid username.
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
