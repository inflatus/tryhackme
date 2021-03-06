#!/usr/bin/python3

import os
from colorama import Fore
from crypt import crypt
from sys import argv
from spwd import getspnam


def main():
    uid = os.getuid()
    if (uid != 0):
        print(Fore.YELLOW + "Use root!")
        exit(1)

    if (len(argv) <= 1):
        print(Fore.YELLOW + "What user's password should we crack?" + Fore.RESET)
        username = input()
    else:
        username = argv[1]

    print(Fore.CYAN + "Cracking your UNIX password for " + Fore.YELLOW + username)

    dict_file = open("10-million-password-list-top-1000000.txt")
    encrypted_password = getspnam(username)[1]

    print(Fore.CYAN + "Encrypted password is " + Fore.YELLOW + encrypted_password)

    count = 0

    for password in dict_file.readlines():
        password = password.rstrip()
        new_password = crypt(password, encrypted_password)

        print(Fore.YELLOW + "Trying password " + Fore.MAGENTA + password)

        if (encrypted_password == new_password):
            print(Fore.GREEN + "Password found!")
            print(Fore.YELLOW + "It took " + Fore.CYAN + str(count))
            print(Fore.RESET + "The cracked password is " + Fore.BLUE + password)
            exit(0)
        else:
            print(Fore.RED + "Password failed")
            count += 1

    print(Fore.RED + "Better luck next time. Try another dictionary" + Fore.RESET)
    exit(1)


if __name__ == "__main__":
    main()
