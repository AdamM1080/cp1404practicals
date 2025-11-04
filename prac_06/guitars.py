"""
CP1404 Practical - Playing with guitar.py
Estimated time: 60 minutes
Actual time: It's late...
"""

from prac_06.guitar import Guitar


def main():
    """My Guitars! - Display guitars entered by user"""
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added")
        name = input("Name: ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        maximum_name_length = max(len(guitar.name) for guitar in guitars)
        print(f"Guitar {i}: {guitar.name:>{maximum_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
