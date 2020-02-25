import matplotlib.pyplot as plt

from numpy import linspace

from cmath import sqrt, sin, cos, tan


def get_y(x):
    """Returns the y value of the mathematical function."""

    y = sx**2 - x**4
    return y



x_val = []
y_val = []
for x in linspace(-10, -0.01, 2000):
    y = get_y(x)

    x_val.append(x)
    y_val.append(y)


for x in linspace(0.01, 10, 2000):
    y = get_y(x)

    x_val.append(x)
    y_val.append(y)

plt.plot(x_val, y_val, linewidth = 1)
plt.show()