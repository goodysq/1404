from car import Car
from random import randint


class UnreliableCar(Car):
    """Initialise a UnreliableCar instance."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car base on reliability"""
        random_num = randint(1, 100)
        if random_num >= self.reliability:
            distance = 0
        distance_drove = super().drive(distance)
        return distance_drove
