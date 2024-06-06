# Email Validator

## Overview

The email validator script checks whether a given email meets specific criteria and determines its validity.

## Features

The email validator script validates email based on common format rules and ensures the presence of `@` and `.` in appropriate places.

## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/AgSilve/validation-projects.git
   ```

2. Navigate to the project directory:
   ```bash
   cd email-validator
   ```

3. Run the script:
   ```bash
   python3 email_validator.py
   ```

4. Enter a email when prompted.

## Implementation Details

The script consists of two main functions:
- `main()`:Prompts the user to enter a email and calls the `is_valid_email()` function to validate it.
- `is_valid_email(email)`: Validates the email against the defined criteria using a regular expression pattern.

## Regular Expression Pattern

The regular expression pattern used for email validation is as follows:
```python
    pattern = r"^[a-zA-Z0-9\.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
```
This regular expression covers common email formats and ensures the basic structure of an email address with the "@" symbol separating the local part and the domain, and at least one dot in the domain part followed by a valid TLD such as .com, .org, .net etc.
## Example

```
$ python3 email_validator.py
Enter email: agspades@proton.me
Valid email.
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
