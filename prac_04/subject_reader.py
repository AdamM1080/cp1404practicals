"""
CP1404/CP5632 Practical04
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_details = load_subject_details(FILENAME)
    print(f"{subject_details}".replace("], [", "],["))
    display_subject_details(subject_details)


def load_subject_details(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_details.append(parts)
    input_file.close()
    return subject_details


def display_subject_details(subject_details):
    """Display various subject details from list."""
    for detail in subject_details:
        print(f"{detail[0]:} is taught by {detail[1]:<12} and has {detail[2]:>3} students.")


main()
