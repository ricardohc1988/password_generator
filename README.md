# Password Generator

This project is a simple Password Generator built using Python and CustomTkinter. It allows users to generate strong and random passwords based on selected criteria, such as including uppercase letters, lowercase letters, numbers, and symbols.

## Features

- **Customizable Password Length:** Choose the length of the password from a range of 4 to 20 characters.
- **Character Set Options:** Select which types of characters to include in the password (uppercase, lowercase, numbers, symbols).
- **Random Password Generation:** Ensures that the generated password includes at least one character from each selected set.
- **Copy to Clipboard:** Easily copy the generated password to the clipboard with a single click.

## Requirements

- Python 3.x
- Pipenv

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/password-generator.git
   ```

2. **Install dependencies:**

   ```bash
   pipenv install
   ```

## Usage

1. Activate the virtual environment and run the application:

   ```bash
   pipenv shell
   python main.py
   ```
2. Open the application.
3. Select the desired password length using the dropdown menu.
4. Choose the types of characters to include by checking the corresponding checkboxes.
5. Click the "Generate Password" button to create a random password.
6. Click the "Copy to Clipboard" button to copy the generated password.
