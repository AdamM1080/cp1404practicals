"""
CP1404 - Practical 01
Ask the user for their name and provide a corresponding greeting/farewell message depending on menu choice.
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""


def main():
    name = input("Enter name: ").title()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")


main()
