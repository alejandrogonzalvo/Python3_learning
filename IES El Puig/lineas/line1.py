import matplotlib.pyplot as plt

from numpy import linspace

from cmath import sqrt


def get_x(x):
    """Returns the x value of the mathematical function."""

    t = sqrt(1 / (x**3 / 3 + x / 3))
    return t

def get_y(y):
    """Returns the y value of the mathematical function."""

    t = 1 / (y**3 / 3 + y / 3)
    return t



x_val = []
y_val = []
for t in linspace(-100, -0.01, 200):
    x = get_x(t)
    y = get_y(t)

    x_val.append(x)
    y_val.append(y)


for t in linspace(0.01, 10, 200):
    x = get_x(t)
    y = get_y(t)

    x_val.append(x)
    y_val.append(y)

plt.plot(x_val, y_val, linewidth = 1)
plt.show()