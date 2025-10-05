"""
CP1404/CP5632 - Practical03
Various file read exercises
"""
# 1.
FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, "w")
out_file.write(name)
out_file.close()

# 2.
FILENAME = "name.txt"
in_file = open(FILENAME, "r")
print(f"Hi {in_file.read()}!")
in_file.close()

# 3.
FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
    print(result)
in_file.close()

# 4.
FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    total = 0
    for line in in_file:
        total += float(line)
print(total)
in_file.close()
