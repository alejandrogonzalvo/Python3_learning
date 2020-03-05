"""

graficas : este programa visualiza una serie de graficas en un espacio 2d

Made by Alejandro Gonzalvo
Github: https://github.com/dahko37/Python3_learning

"""


import matplotlib.pyplot as plt

from numpy import linspace

from cmath import sqrt, sin, cos, tan, pi



def espiral_1():
    """Representa la función R(t) = t / 2pi para: 0 <= t <= 2pi"""
    
    x_val = []
    y_val = []
    
    for t in linspace(0, 4*pi, 2000):
        r = t / (2*pi)
        x = r * cos(t)
        y = r * sin(t)
        x_val.append(x)
        y_val.append(y)

    plt.plot(x_val, y_val)
    plt.show()


def espiral_2():
    """Representa la función R(t) = 1 - t / 2pi para: 0 <= t <= 2pi"""

    x_val = []
    y_val = []
    
    for t in linspace(0, 2*pi, 2000):
        r = 1 - (t / (2*pi))
        x = r * cos(t)
        y = r * sin(t)
        x_val.append(x)
        y_val.append(y)

    plt.plot(x_val, y_val)
    plt.show()


def corazon_1():
    """
    Representa la ecuacion parametrica:

    x = (1 + cost)cost
    y = (1 + cost)sent

    para: 0 <= t <= 2pi

    """

    x_val = []
    y_val = []

    for t in linspace(0, 2*pi, 2000):
        x = (1 + cos(t))*cos(t)
        y = (1 + cos(t))*sin(t)

        x_val.append(x)
        y_val.append(y)

    plt.plot(x_val, y_val)
    plt.show()


def corazon_2():
    """
    Representa la ecuacion parametrica:

    x = (1 - cost)cost
    y = (1 - cost)sint

    para: 0 <= t <= 2pi

    """

    x_val = []
    y_val = []

    for t in linspace(0, 2*pi, 2000):
        x = (1 - cos(t))*cos(t)
        y = (1 - cos(t))*sin(t)

        x_val.append(x)
        y_val.append(y)

    plt.plot(x_val, y_val)
    plt.show()


def flor_1():
    """
    
    Representa la equacion parametrica:
    
    x = 2.5*sin**2(-5*t)*2**cos(cos(4.28*2.3*t))
    y = 2.5*sin(sin(-5*t))*cos**2(4.28*2.3*t)

    para: -6 <= t <= 6
    
    """

    x_val = []
    y_val = []

    for t in linspace(-8, 8, 50000):
        x = 2.5*(sin(-5*t)**11)*(2**cos(cos(4.28*2.3*t)))
        y = 2.5*sin(cos(-5*t))*cos(4.28*2.3*t)**3
        x_val.append(x)
        y_val.append(y)

    plt.plot(x_val, y_val, linewidth = 0.5)
    plt.show()

flor_1()


def main():
    """Ejecuta el programa principal"""
