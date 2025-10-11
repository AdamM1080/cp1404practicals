"""
CP1404/CP5632 Practical04
Various list warmups.
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = True
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1.
numbers = ["ten"] + numbers
print(numbers)

# 2.
numbers += [1]
print(numbers)

# 3.
print(numbers[2:])

# 4.
print(9 in numbers)