import matplotlib.pyplot as plt


squares = []
cubes = []

for i in range(10):
    z = i**2
    squares.append(z)

    z = i**3
    cubes.append(z)

plt.plot(squares, linewidth = 5)
plt.plot(cubes, linewidth = 5)

plt.title("Squares and cubes", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Exponential Value", fontsize = 14)

plt.tick_params(axis='both', labelsize = 14)

plt.show()
    