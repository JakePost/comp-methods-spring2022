# Exercise 5.12: The Stefan-Boltzmann Constant

import numpy as np
import astropy.units as u
import scipy.constants as cons

print(f"Reduced Planks Constant: {cons.hbar * (u.m ** 2) * u.kg / u.s}")


def trapezoidal(f, n, a, b):
    h = (b - a) / n
    sum_part = sum(f(a + k * h) for k in range(1, n))

    return h * (f(a) / 2 + f(b) / 2 + sum_part)


def func(x):
    return (x ** 3) / (np.exp(x) - 1)


sigma = ((cons.k ** 4) / (4 * (cons.pi ** 2) * (cons.c ** 2) * (cons.hbar ** 3))) * trapezoidal(func, 10000, 10e-14, 100)
units = u.W * u.m ** -2 * u.K ** -4

print(f"Known Value: {cons.sigma * units}")
print(f"Calculated Value: {sigma * units}")
