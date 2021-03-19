import os
from getpass import getpass
import crypt

SHADOW_LOC = '/etc/shadow' # Specify Shadow file location


def main():
    if os.access(SHADOW_LOC, os.F_OK):  # Make sure Shadow file exists.
        attempt = 0
        while attempt < 3: # User has 3 attempts to guess the credentials
            shadowRead = open(SHADOW_LOC, mode='r')  # Read from Shadow file
            user = input("Specify User Account: ")
            password = getpass("Type your password: ")
            userFound = False
            for line in shadowRead.readlines():  # Make sure user exists
                if (user in line):
                    userFound = True
                    line = line.strip()  # Remove blank space
                    line = line.replace("\n", "").split(":")
                    if line[1] not in ['x', '*', '!']:
                        user = line[0].strip()                      # Get the name of user
                        hashedPass = line[1].strip()                # Get the value of the hashed Pass
                        hashType = hashedPass.split("$")[1]         # Get the hash type
                        salt = hashedPass.split("$")[2]             # Get the value of salt
                        insalt = "$" + hashType + "$" + salt + "$"  # Combine hash type and salt
                        hash = crypt.crypt(password, insalt)        # Get the hash of password with salt prepended
            if userFound is True and hash == hashedPass:  #
                print("Welcome '{}'!".format(user))
                break
            else:
                print("WRONG CREDENTIALS!")
                attempt = attempt + 1
    else:  # Alert if shadow file does not exist
        print("Shadow file does not exist at "), SHADOW_LOC


if __name__ == '__main__':
    main()
