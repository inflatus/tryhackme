#!/usr/bin/python3

import os
from crypt import crypt
from sys import argv
from spwd import getspnam


def main():
    uid = os.getuid()
    if (uid != 0):
        print("Use root!")
        exit(1)

    if (len(argv) <= 1):
        print("What user's password should we crack?")
        username = input()
    else:
        username = argv[1]

    print("Cracking your UNIX password for " + username)

    dict_file = open("10-million-password-list-top-1000000.txt")
    encrypted_password = getspnam(username)[1]

    print("Encrypted password is " + encrypted_password)

    count = 0

    for password in dict_file.readlines():
        password = password.rstrip()
        new_password = crypt(password, encrypted_password)

        print("Trying password " + password)

        if (encrypted_password == new_password):
            print("Password found!")
            print("It took " + str(count))
            print("The cracked password is " + password)
            exit(0)
        else:
            print("Password failed")
            count += 1

    print("Better luck next time. Try another dictionary")
    exit(1)


if __name__ == "__main__":
    main()
