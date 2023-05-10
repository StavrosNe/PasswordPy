# Password Manager Application

This is a small password manager application that I created as a hobby project to learn new things using Python. The application allows users to store and manage their passwords securely using encryption.

## Features

- User sign-up and login
- Data encryption using AES 256 CBC and unique IV for each data entry
- Password hashing using salt and pepper
- Connection to websites through the app
- Strong password and encryption key requirements

## Requirements

- Python 3.x
- Pillow==9.5.0
- pycryptodome==3.17
- customtkinter==5.1.2
- googlesearch-python==1.2.3

## Installation

1. Clone the repository to your local machine.
2. Install the required libraries using pip: `pip install -r requirements.txt`.
3. Run the application using the command `python password_manager.py`.

## Usage

1. Sign up for an account using the application.
2. Log in to your account using your username and password.
3. Enter a strong encryption key to protect your data.
4. Add new passwords by entering the application name, username, and password.
5. Connect to websites through the app by entering the website name and clicking "Connect".

## Security

- Passwords are stored hashed in a local database using salt and pepper.
- Data is encrypted using AES 256 CBC and unique IV for each data entry.
- The encryption key is not stored anywhere and must be entered by the user.
- Passwords and encryption keys must meet strong requirements for length and complexity.
- Encryption key: At least 12 characters long must contain caps,numbers,special characters and no spaces.
- Password : At least 8 characters long must contain caps,numbers,special characters and no spaces.

## Disclaimer
This application is provided for educational and informational purposes only. 
The developer is not responsible for any loss or damage that may result from the use of this application. 
It is the responsibility of the user to ensure that all passwords and other sensitive information are kept secure and that best practices for password management are followed. The developer does not guarantee the security of any data stored or transmitted by this application. Use this application at your own risk.


