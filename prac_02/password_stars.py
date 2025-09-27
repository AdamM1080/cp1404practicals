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