"""
CP1404/CP5632 - Practical03
Answer the following questions:
1. When will a ValueError occur?
When an inappropriate argument value is entered, such as the string "asdf".
2. When will a ZeroDivisionError occur?
When the second argument to a division or modulo operation was zero, such as "1/0".
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, but the exception method is simpler, isn't it? I assume that's the point?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
