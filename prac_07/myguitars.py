"""
CP1404/CP5632 Practical - My Guitars!
Estimated time: 30 minutes
Actual time: An hour or two
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """My Guitars! - Add and display guitars entered by user"""
    guitars = load_guitars(FILENAME)
    guitars.sort()
    print("My Guitars!")
    get_new_guitars(guitars)
    display_guitars(guitars)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file"""
    guitars = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            part = line.strip().split(",")
            name, year, cost = part[0], part[1], part[2]
            guitars.append(Guitar(name, year, cost))
    in_file.close()
    return guitars


def get_new_guitars(guitars):
    """Get new guitars from user input"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        guitars.sort()
        print(f"{new_guitar} added")
        name = input("Name: ")


def display_guitars(guitars):
    """Display guitars entered by user"""
    print("These are my guitars:")
    max_name_length = max(len(g.name) for g in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_status = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_status}")


def save_guitars(filename, guitars):
    """Save guitars entered by user to file"""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost:.2f}", file=out_file)
    out_file.close()


main()
