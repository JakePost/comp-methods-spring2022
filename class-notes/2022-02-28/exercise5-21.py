# 5.21: Electric field of a charge distribution

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons

# [x, y, charge]
from matplotlib.colors import LogNorm, SymLogNorm

charges = [[45, 50, 1], [55, 50, -1]]


def calc_potential(x, y):
    pot = 0

    for charge in charges:
        if charge[0] == x and charge[1] == y:
            continue

        r = np.sqrt((charge[0] - x) ** 2 + (charge[1] - y) ** 2)
        pot += charge[2] / (4 * cons.pi * cons.epsilon_0 * r ** 2)

    return pot


potentials = np.zeros((100, 100))

for j in range(0, 100):
    for i in range(0, 100):
        potentials[j, i] = calc_potential(i, j)

print(potentials.size, potentials.shape)

plt.imshow(potentials, origin='lower', cmap='bwr', norm=SymLogNorm(10E-01))
plt.colorbar()

plt.show()


