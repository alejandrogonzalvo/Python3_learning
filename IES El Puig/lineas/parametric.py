import matplotlib.pyplot as plt

from numpy import linspace, cos, sin

from cmath import sqrt


def get_x(x):
    """Returns the x value of the mathematical function."""

    t = cos(x)
    return t

def get_y(y):
    """Returns the y value of the mathematical function."""

    t = sin(y)
    return t



x_val = []
y_val = []
for t in linspace(-10, -0.01, 20000):
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