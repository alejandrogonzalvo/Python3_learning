import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    rw = RandomWalk(500000)
    rw.walk()

    point_numbers = list(range(rw.points)) 
    plt.scatter(
        rw.x_val,
        rw.y_val,
        c=point_numbers,
        cmap = 'Blues',
        edgecolor='none',
        s=15
    )

    plt.scatter(0, 0, c='green', edgecolors = 'none', s = 100)
    plt.scatter(
        rw.x_val[-1],
        rw.y_val[-1],
        c = 'red',
        edgecolors = 'none',
        s = 100 
    )

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    i = input("Make another walk? (y/n): ")
    if i == 'n':
        break
