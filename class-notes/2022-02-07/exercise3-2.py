# Exercise 3.2: Curve plotting
# Although the plot function is designed primarily for plotting standard xy graphs,
# it can be adapted for other kinds of plotting as well.
#
# 1) Make a plot of the so-called deltoid curve, which is defined parametrically by the equations,
#    x = 2 * cos(theta) + cos(2 * theta), y = 2 * sin(theta) - sin(2 * theta), where 0 <= theta <= 2 * pi.
#    Take a set of values of theta between zero and 2pi and calculate x and y for each from the equations above,
#    plot y as function of x
#
# 2) Taking this approach a step futher, one can make a polar plot r=f(theta) for some function f by calculating
#    r for a range of values of theta and then converting r and theta to Cartesian coordinates using the standard
#    equations x = r * cos(theta), y = r * sin(theta). Use this method to make a plot of the Galilean spiral,
#    r = theta ** 2 for 0 <= theta <= 10 * pi
#
# 3) Using the same methods, make a polar plot of "Fey's function"
#    r = exp(cos(theta)) - 2 * cos(4 * cos(theta)) + sin(theta / 12) ** 5
#    in the range - <=theta <= 24 * pi.

import matplotlib.pyplot as plt
import numpy as np


def deltoid(theta) -> tuple[float, float]:
    return 2 * np.cos(theta) + np.cos(2 * theta), 2 * np.sin(theta) - np.sin(2 * theta)


def galilean_spiral(theta) -> tuple[float, float]:
    r = theta ** 2
    return r * np.cos(theta), r * np.sin(theta)


def fey_spiral(theta) -> tuple[float, float]:
    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta / 12) ** 5
    return r * np.cos(theta), r * np.sin(theta)


deltoid_x, deltoid_y = deltoid(np.linspace(0, 2 * np.pi, 1000))
spiral_x, spiral_y = galilean_spiral(np.linspace(0, 10 * np.pi, 1000))
fey_x, fey_y = fey_spiral(np.linspace(0, 24 * np.pi, 1000))

figure, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].set_title("Deltoid")
axes[0].plot(deltoid_x, deltoid_y)

axes[1].set_title("Galilean Spiral")
axes[1].plot(spiral_x, spiral_y)

axes[2].set_title("Fey's Function")
axes[2].plot(fey_y, fey_x)

plt.show()
