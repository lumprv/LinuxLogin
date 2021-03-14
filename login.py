import os
from getpass import getpass
from hashlib import sha256

username = input("Username: ")
password = getpass("Password: ")

if username == "admin" and password == "password":
    print("Welcome '{}'!".format(username))
else:
    print("Wrong credentials!")

