from random import choice



class RandomWalk():
    """A class to generate random walks"""

    def __init__(self, points = 500000):
        """Initialize atributes of the walk"""

        self.points = points

        self.x_val = [0]
        self.y_val = [0]



    def walk(self):
        """Calculate all the points in the walk"""

        def get_step():
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4, 5])
            step = direction * distance

            return step


        while len(self.x_val) < self.points:

            x_step = get_step()
            y_step = get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step

            self.x_val.append(next_x)
            self.y_val.append(next_y)

