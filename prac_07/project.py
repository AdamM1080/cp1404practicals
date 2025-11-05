"""
CP1404/CP5632 Practical - Project class
Estimated time: 30 minutes
Actual time: An hour or two
"""

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """"""
        return f"{self.name} {self.start_date} {self.priority} {self.cost_estimate} {self.completion_percentage}"

