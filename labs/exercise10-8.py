import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

n = 1000000
rand.seed(3141592653)


dist = rand.random(n)  # Random numbers with uniform distribution
p_dist = [x ** 2 for x in dist]  # Transform uniform distribution into probability distribution


def g(x):
    return 2 / (np.exp(x) + 1)


mean = np.mean(g(p_dist))

print(mean)
