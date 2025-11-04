"""
CP1404 Practical - Client code to test Guitar class
Estimated time: 45 minutes
Actual time: 15 minutes
"""

from prac_06.guitar import Guitar


def main():
    gibson_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 50)
    print(f"{gibson_ces.name} get_age() - Expected 100. Got {gibson_ces.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
    print(f"{gibson_ces.name} is_vintage() - Expected True. Got {gibson_ces.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    main()
