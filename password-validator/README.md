# Password Validator

## Overview

The Password Validator script validates the strength of a password based on specific criteria, ensuring it meets security standards. This script prompts the user to enter a password and then validates it against predefined rules.

## Features

- Validates passwords based on length, character types, and absence of spaces.
- Provides feedback on whether the password is valid or not.
- Can be easily integrated into other Python projects or used as a standalone tool.

## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/AgSilve/validation-projects.git
   ```

2. Navigate to the project directory:
   ```bash
   cd password-validator
   ```

3. Run the script:
   ```bash
   python3 password_validator.py
   ```

4. Enter a password when prompted.

## Validation Criteria

The script checks the following criteria for password validation:

- Minimum length of 8 characters.
- Contains at least one uppercase letter.
- Contains at least one lowercase letter.
- Contains at least one digit.
- Contains at least one special character.
- Does not contain spaces.

## Example

```
$ python3 password_validator.py
Enter password: G0jo!sB@ck
Valid password.
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE]([MIT-LICENSE.txt](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)) file for details.
