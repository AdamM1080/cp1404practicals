"""
CP1404/CP5632 Practical
Silver service taxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Fancy taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize SilverServiceTaxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return string representation of SilverServiceTaxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return new fare with flagfall added"""
        return super().get_fare() + self.flagfall
