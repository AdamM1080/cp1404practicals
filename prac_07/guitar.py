"""
CP1404/CP5632 Practical - Guitar class
Estimated time: 30 minutes
Actual time: 15 minutes
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        return self.get_age() > 50

    def __lt__(self, other):
        return self.year < other.year
