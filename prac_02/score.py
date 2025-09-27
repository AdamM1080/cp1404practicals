"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    while score <= 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score: "))
    if score < 50:
        print("Bad")
    elif score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")


main()
