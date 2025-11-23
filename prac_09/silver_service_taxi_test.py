"""
CP1404/CP5632 Practical
Silver service taxi test object
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare: ${fare:.2f}")
    assert (fare - 48.80) < 0.01, f"Expected fare 48.80, Actual fare: ${fare:.2f}"


if __name__ == "__main__":
    main()
