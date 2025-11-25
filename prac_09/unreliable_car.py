"""
CP1404/CP5632 Practical
Unreliable car class
"""

from random import randint
from prac_09.car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance = randint(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        return 0
