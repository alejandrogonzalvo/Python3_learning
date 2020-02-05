import matplotlib.pyplot as plt


primes = []
nonprimes = []
for i in range(2, 100000):
    for d in range(2, i):

        if i % d == 0:
            nonprimes.append(i)
            break

    if i not in nonprimes:
        primes.append(i)


plt.plot(primes, linewidth = 5)
plt.plot(nonprimes, linewidth = 5)

plt.show()