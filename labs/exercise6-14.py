import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import scipy.constants as cons

w = 1 * u.nm
m = cons.electron_mass * u.kg
V = 20 * u.eV


def y1(e):
    v = float(((w ** 2) * m * (e * u.eV)) / (2 * (cons.hbar * u.J * u.s) ** 2))

    return np.tan(np.sqrt(v))


def y2(e):
    return np.sqrt((V - (e * u.eV)) / (e * u.eV))


def y3(e):
    return - np.sqrt((e * u.eV) / (V - (e * u.eV)))


def bin_search(f, g, x1, x2):
    left = x1
    right = x2
    mid = 0

    while abs(left - right) > 10e-5:
        mid = (left + right) / 2

        left_diff = f(left) - g(left)
        mid_diff = f(mid) - g(mid)

        if np.sign(left_diff) == np.sign(mid_diff):
            left = mid
        else:
            right = mid

    return mid


first = bin_search(y1, y2, 0, 0.5)
second = bin_search(y1, y3, 1, 1.5)
third = bin_search(y1, y2, 2.5, 3)
forth = bin_search(y1, y3, 4.5, 5.5)
fifth = bin_search(y1, y2, 7, 8.5)
sixth = bin_search(y1, y3, 10.5, 11.5)

x_plt = np.linspace(0, 20, 1000)
y1_plt = np.array([y1(x) for x in x_plt])
y2_plt = [y2(x) for x in x_plt]
y3_plt = [y3(x) for x in x_plt]

y1_plt[:-1][np.diff(y1_plt) < 0] = np.nan

plt.plot(x_plt, y1_plt, c='r')
plt.plot(x_plt, y2_plt, c='g')
plt.plot(x_plt, y3_plt, c='b')

plt.vlines(first, -15, 15, linestyles='dashed')
plt.vlines(second, -15, 15, linestyles='dashed')
plt.vlines(third, -15, 15, linestyles='dashed')
plt.vlines(forth, -15, 15, linestyles='dashed')
plt.vlines(fifth, -15, 15, linestyles='dashed')
plt.vlines(sixth, -15, 15, linestyles='dashed')

plt.ylim(-15, 15)
plt.show()

