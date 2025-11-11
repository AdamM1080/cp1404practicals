"""
CP1404/CP5632 Practical - Guitar class
Estimated time: 30 minutes
Actual time: 15 minutes
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object."""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Return string representation of Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return age of Guitar"""
        return 2025 - self.year

    def is_vintage(self):
        """Return True if Guitar is vintage"""
        return self.get_age() > 50

    def __lt__(self, other):
        """Return if age of guitar is less than other guitar"""
        return self.year < other.year
