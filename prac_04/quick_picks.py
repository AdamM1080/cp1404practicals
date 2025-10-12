"""
CP1404/CP5632 Practical
Quick picks program that asks a user for a number of picks and generates random numbers in lines.
"""
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Get user input of picks and display corresponding random numbers in lines"""
    choice = int(input("How many quick picks?: "))
    for i in range(choice):
        numbers = []
        while len(numbers) < NUMBERS_PER_PICK:
            number = randint(MIN_NUMBER, MAX_NUMBER)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        print(" ".join(f"{number:2}" for number in numbers))


main()
