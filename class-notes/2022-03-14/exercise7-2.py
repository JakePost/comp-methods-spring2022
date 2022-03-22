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

    return [np.sum([y[n] * cm.exp(-2j * cm.pi * k * n / N) for n in range(N)]) for k in range(N // 2 + 1)]


ft = fourier_transform(df.iloc[:, 1])

ft_2 = [np.sqrt(ft[x] * np.conj(ft[x])) for x in range(len(ft))]

plt.bar(range(len(ft)), ft_2)
plt.ylabel('$|C_k|^2$')
plt.xlabel('k')
plt.xlim(-1, 50)
plt.show()
