# !/usr/bin/python3.5


class Restaurant():
    """A simple attempt to represent a restaurant irl"""

    def __init__(self, name, cuissine, ophour, clhour):
        self.name = name
        self.cuissine = cuissine
        self.ophour = ophour
        self.clhour = clhour

    def describe(self):
        print(self.cuissine.title() + ' ' + self.name.title() + ' opens Monday to Saturday from ' + str(self.ophour) + ' to ' + str(self.clhour))


my_rest = Restaurant('casa pepe', 'asador', 8, 24)
my_rest.describe()
