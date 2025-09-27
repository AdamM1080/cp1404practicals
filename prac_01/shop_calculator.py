"""
CP1404 - Practical 01
Work out the total price for a number of items, each with different prices.
"""


def main():
    total_price = 0
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    for n in range(number_of_items):
        item_price = float(input("Item price: "))
        total_price += item_price
    if total_price > 100:
        total_price -= total_price / 10
    print(f"The total price is ${total_price:.2f}")


main()