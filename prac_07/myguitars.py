""""""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """My Guitars! - Display guitars entered by user"""
    guitars = load_guitar_data(FILENAME)
    guitars.sort()
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        print(f"{guitar} added")
        name = input("Name: ")
    display_guitar_data(guitars)


def load_guitar_data(filename):
    guitars = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            part = line.strip().split(",")
            name, year, cost = part[0], part[1], part[2]
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitar_data(guitars):
    """Display guitars entered by user"""
    print("These are my guitars:")
    max_name_length = max(len(g.name) for g in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_status = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_status}")



main()