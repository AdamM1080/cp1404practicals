"""
CP1404 - Practical01
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SALES_THRESHOLD = 1000
BONUS_THRESHOLD_LOW = 0.10
BONUS_THRESHOLD_HIGH = 0.15


def main():
    sales = float(input("Enter sales: "))
    while sales >= 0:
        if sales < 1000:
            bonus = sales * 0.1
        else:
            bonus = sales * 0.15
        print(f"Your sales bonus is: ${bonus:.2f}")
        sales = float(input("Enter sales: "))
    print("Farewell")


main()
