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


x_plt = np.linspace(0, 20, 1000)
y1_plt = np.array([y1(x) for x in x_plt])
y2_plt = [y2(x) for x in x_plt]
y3_plt = [y3(x) for x in x_plt]

y1_plt[:-1][np.diff(y1_plt) < 0] = np.nan

plt.plot(x_plt, y1_plt, c='r')
plt.plot(x_plt, y2_plt, c='g')
plt.plot(x_plt, y3_plt, c='b')
plt.ylim(-15, 15)
plt.show()

