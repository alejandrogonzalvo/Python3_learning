from random import randint

class Dice():
    """A representation of a dice, with X sides."""

    def __init__(self, sides = 6):
        """
        
        If the user doesn't select a specific number of sides,
        we assume its a six-sided dice.

        """

        self.sides = sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.sides)