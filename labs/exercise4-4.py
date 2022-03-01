# Exercise 4.4

import math
import numpy as np
import time


def yk(k, h):
    return np.sqrt(1 - ((-1 + (h * k)) ** 2))


def riemann(f, n, a, b):
    h = (b - a) / n
    return sum(h * f(k, h) for k in range(1, n))


start = time.time()
r = riemann(yk, 1000000, -1, 1)
end = time.time()

print(r, (math.pi/2))
print(f"Program took {end-start} seconds to run")
