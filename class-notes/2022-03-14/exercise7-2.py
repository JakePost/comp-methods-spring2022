import numpy as np
import cmath as cm
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sunspots.txt', sep='\t', header=None, names=['Month', 'Sunspot Number'])

# plt.plot(df.iloc[:, 0], df.iloc[:, 1])
# plt.ylabel("Sunspot Numbers")
# plt.xlabel("Month")
# plt.show()


# noinspection PyPep8Naming
def fourier_transform(y):
    N = len(y)

    c = np.zeros(N // 2 + 1, complex)

    for k in range(N // 2 + 1):
        for n in range(N):
            c[k] += y[n] * cm.exp(-2j * cm.pi * k * n / N)

    return c


ft = fourier_transform(df.iloc[:, 1])

plt.plot(range(len(ft)), ft ** 2)
plt.show()
