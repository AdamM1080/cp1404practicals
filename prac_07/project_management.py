"""
CP1404/CP5632 Practical - Project Management
Estimated time: 30 minutes
Actual time: Long one
"""

import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Pythonic project management main menu"""
    print("Welcome to Pythonic Project Management")
    selected_filename = DEFAULT_FILENAME
    projects = load_projects(selected_filename)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            selected_filename = input("Enter filename to load: ")
            load_projects(selected_filename)
        elif choice == "S":
            save_projects(selected_filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            # update_project(projects)
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_confirmation = input("Would you like to save to projects.txt? ")
    if save_confirmation == "Y":
        save_projects(selected_filename, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(selected_filename):
    """Load projects from a file"""
    projects = []
    number_of_projects_loaded = 0
    with open(selected_filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            project_part = line.split("\t")
            name, start_date, priority, cost_estimate, completion_percentage = project_part[0], project_part[1], int(
                project_part[2]), float(project_part[3]), int(project_part[4])
            convert_date_string(start_date)
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
            number_of_projects_loaded += 1
        print(f"Loaded {len(projects)} from {selected_filename}")
    in_file.close()
    return projects


def convert_date_string(start_date):
    """Convert start date string to a datetime object"""
    return datetime.datetime.strptime(start_date, "%d/%m/%Y").date()


def save_projects(selected_filename, projects):
    """Save projects to file"""
    with open(selected_filename, "w", encoding="utf-8") as out_file:
        out_file.readline()
        for name, start_date, priority, cost_estimate, completion_percentage in projects:
            print(f"{name}{start_date}{priority}{cost_estimate}{completion_percentage}", sep="\t", file=out_file)
    out_file.close()


def display_projects(projects):
    """Display projects entered by user"""
    incomplete_status = [project for project in projects if project.completion_percentage < 100]
    complete_status = [project for project in projects if project.completion_percentage == 100]
    incomplete_status.sort()
    complete_status.sort()
    print("Incomplete projects:")
    for project in incomplete_status:
        print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")
    print("Completed projects:")
    for project in complete_status:
        print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")


def filter_projects_by_date(projects):
    """Filter projects by date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    filter_date = convert_date_string(date_string)
    filtered_projects = [project for project in projects if convert_date_string(project.start_date) >= filter_date]
    filtered_projects.sort()
    for project in filtered_projects:
        print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")


def add_new_project(projects):
    """Add a new project"""
    print("let's add a new project")
    name = input("Name: ").strip()
    start_date = input("Start date: ").strip()
    start_date_string = convert_date_string(start_date)
    priority = input("Priority: ").strip()
    cost_estimate = float(input("Cost estimate: ").strip())
    completion_percentage = int(input("Percent complete: ").strip())
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    return new_project


# def update_project():


if __name__ == '__main__':
    main()
