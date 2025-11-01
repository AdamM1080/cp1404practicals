class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        name = "Gibson L-5 CES"
        year = 1922
        cost = 16035.40
        print(f"My guitar: {name}, first made in {year}")
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False
