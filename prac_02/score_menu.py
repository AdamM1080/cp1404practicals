"""
CP1404/CP5632 - Practical02
Program to get a valid score, then determine a result and print a corresponding number of stars
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Gets a valid score"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_result(score):
    """Determine results from score status"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def print_stars(score):
    """Prints stars from the length of entered score"""
    print("*" * int(score))


main()
