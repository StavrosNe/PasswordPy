# PyPass
This a small password manager application that I created as hobby project to learn new things using python.
The user has to sign up first and then can login to the app.
After the user is loged in, the user is promted to enter an encryption key. 
Using this key the app can encrypt the users data for example:
application name : GitHub , username: username1 , password : password123 
The password is stored hashed in a local database (salt+pepper).
The data is encrypted using AES 256 CBC and for every data entered a unique IV is used.
The encryption key is not stored anywhere.
Also the user can connect to website through the app.
Encryption key : At least 12 characters long must contain caps,numbers,special characters and no spaces
Password : At least 8 characters long must contain caps,numbers,special characters and no spaces
I am using these libraries:
  Pillow==9.5.0
  pycryptodome==3.17
  customtkinter==5.1.2
  googlesearch-python==1.2.3
  
