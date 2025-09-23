"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# def example():
#     for i in range(1, 21, 2):
#         print(i, end=" ")
#     print()

# def part_a():
#     for i in range(0, 101, 10):
#         print(i, end=" ")
#     print()


# def part_b():
#     for i in range(20, 0, -1):
#         print(i, end=" ")
#     print()

def part_c():
    number_of_stars = int(input("Enter the number of stars: "))
    for i in range(number_of_stars):
        print()
    print("*", end="")


def part_d():
    number_of_stars = int(input("Enter the number of stars: "))
    for i in range(number_of_stars):
        print("*", end = "")
    print()



# example()
# part_a()
# part_b()
# part_c()
part_d()