import os
from getpass import getpass
import crypt

SHADOW_LOC = '/etc/shadow'


def main():
    if os.access(SHADOW_LOC, os.F_OK):  # Make sure Shadow file exists.
        attempt = 0
        while attempt < 3:
            shadowRead = open(SHADOW_LOC, mode='r')
            user = input("Specify User Account: ")
            password = getpass("Type your password: ")
            userFound = False
            for line in shadowRead.readlines():  # Make sure user exists
                if (user in line):
                    userFound = True
                    line = line.strip()  # Remove blank space
                    line = line.replace("\n", "").split(":")
                    if line[1] not in ['x', '*', '!']:
                        user = line[0].strip()
                        hashedPass = line[1].strip()
                        hashType = hashedPass.split("$")[1]
                        salt = hashedPass.split("$")[2]
                        insalt = "$" + hashType + "$" + salt + "$"
                        hash = crypt.crypt(password, insalt)
            if userFound is True and hash == hashedPass:  # Alert if user does not exist
                print("Welcome '{}'!".format(user))
                break
            else:
                print("WRONG CREDENTIALS!")
                attempt = attempt + 1
    else:  # Alert if shadow file does not exist
        print("Shadow file does not exist at "), SHADOW_LOC


if __name__ == '__main__':
    main()
