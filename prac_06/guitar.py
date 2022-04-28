today = 2022
vintage = 50


class Guitar:
    """Information of guitar"""

    def __init__(self, name="", year=0, cost=0):
        """constructor in guitar oriented concepts"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar in string"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """get age of guitar base on today"""
        return today - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage base on it's age"""
        return self.get_age() >= vintage
