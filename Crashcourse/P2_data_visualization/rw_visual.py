import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    rw = RandomWalk()
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

    plt.show()

    i = input("Make another walk? (y/n): ")
    if i == 'n':
        break
