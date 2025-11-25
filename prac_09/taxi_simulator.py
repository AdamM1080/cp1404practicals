"""
CP1404/CP5632 Practical
Taxi simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program"""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.0
    current_taxi = None
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis, current_taxi):
    """Choose a taxi"""
    print("Taxis available: ")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice >= 0 or taxi_choice <= len(taxis):
            current_taxi = taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return current_taxi


def drive_taxi(taxi):
    """Drive a taxi"""
    taxi.start_fare()
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        distance = 0
    taxi.drive(distance)
    return taxi.get_fare()


def display_taxis(taxis):
    """Display the taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
