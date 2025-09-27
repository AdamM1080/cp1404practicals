"""
CP1404/CP5632 - Practical02
Program that gets a valid password and prints a number of corresponding stars
"""

MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter the password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Enter the password: ")
    return password


main()
