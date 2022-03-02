# 5.21: Electric field of a charge distribution

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tik
import scipy.constants as cons
from sklearn.preprocessing import normalize

# Sample space
h = 10E-5

# [x, y, charge]
charges = [[45, 50, 1], [55, 50, -1]]


def calc_potential(x, y):
    pot = 0

    for charge in charges:
        if charge[0] == x and charge[1] == y:
            continue

        r = np.sqrt(((charge[0] - x) ** 2) + ((charge[1] - y) ** 2))
        pot += charge[2] / r

    return pot / 4 * cons.pi * cons.epsilon_0


def partial_x(f, x, y):
    return (f(x + h / 2, y) - f(x - h / 2, y)) / h


def partial_y(f, x, y):
    return (f(x, y + h / 2) - f(x, y - h / 2)) / h


potentials = np.zeros((100, 100))

for j in range(0, 100):
    for i in range(0, 100):
        potentials[j, i] = calc_potential(i, j)

electric_field_x = np.zeros((100, 100))
electric_field_y = np.zeros((100, 100))

for j in range(0, 100):
    for i in range(0, 100):
        electric_field_x[j, i] = partial_x(calc_potential, i, j)
        electric_field_y[j, i] = partial_y(calc_potential, i, j)

electric_field_x = normalize(electric_field_x)
electric_field_y = normalize(electric_field_y)
ef_mag = np.sqrt(electric_field_x ** 2 + electric_field_y ** 2)

plt.figure(figsize=(12, 8))
plt.rc('font', size=20)

plt.quiver(range(0, 100), range(0, 100), electric_field_x, electric_field_y, ef_mag, cmap='rainbow', width=0.0015)

plt.imshow(normalize(potentials), origin='lower', cmap='coolwarm')
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 101, 10))

plt.gca().xaxis.set_major_formatter(tik.FormatStrFormatter('%d cm'))
plt.gca().yaxis.set_major_formatter(tik.FormatStrFormatter('%d cm'))
for label in plt.gca().xaxis.get_majorticklabels():
    label.set_rotation(-90)

cbar = plt.colorbar()
cbar.set_label("Normalized Electric Potential (C)")

plt.tight_layout()
plt.show()
