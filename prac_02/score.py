"""
CP1404/CP5632 - Practical
Program to determine score status of a user, generate a random score and print the results of both.
"""
from random import randint


def main():
    """Determine score status, random score and print results"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = randint(0, 100)
    print(random_score)
    result = determine_result(random_score)
    print(result)


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


main()
