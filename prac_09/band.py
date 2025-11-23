"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band class using association"""

    def __init__(self, name):
        """Initialize band class"""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a band."""
        member_string = ", ".join(str(musician) for musician in self.members)
        return f"{self.name} ({member_string})"

    def add(self, musician):
        """Add new musician to band"""
        self.members.append(musician)

    def play(self):
        """Return each musicians role in band"""
        results = [member.play() for member in self.members]
        return "\n".join(results)
