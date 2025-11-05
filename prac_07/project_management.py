"""
CP1404/CP5632 Practical - Project Management
Estimated time: 30 minutes
Actual time: Long one
"""

# from datetime import date
from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """"""
    print("Welcome to Pythonic Project Management")
    current_filename = DEFAULT_FILENAME
    projects = load_projects(current_filename)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            current_filename = input("Enter filename: ")
            load_projects(current_filename)
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
            choice = input(">>> ").upper()
        print(MENU)
        choice = input(">>> ").upper()
    # save_confirmation = input("Would you like to save to projects.txt? ")
    # if save_confirmation == "Y":
    #     save_projects(selected_filename)
    # print("Thank you for using custom-built project management software.")



def load_projects(current_filename):
    """Load projects from a file"""
    projects = []
    number_of_projects_loaded = 0
    with open(current_filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            project_part = line.split("\t")
            name, start_date, cost_estimate, completion_percentage = project_part[0], project_part[1], project_part[2], project_part[3]
            projects.append(Project(name, start_date, cost_estimate, completion_percentage))
            number_of_projects_loaded += 1
        print(f"Loaded {len(projects)} from {current_filename}")
    in_file.close()
    return projects, number_of_projects_loaded


# def save_projects(selected_filename):
#     """Save projects to file"""


# def display_projects():
#
# def filter_projects_by_date():
#
# def add_new_project():
#
# def update_project():



if __name__ == '__main__':
    main()