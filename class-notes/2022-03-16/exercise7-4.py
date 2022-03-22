import numpy as np
import numpy.fft as fft
import cmath as cm
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dow.txt', sep='\t', header=None, names=['Closing Value'])

# plt.plot(range(len(df.index)), df.iloc[:, 0])
# plt.show()


c = fft.rfft(df.iloc[:, 0])

# plt.bar(range(len(c)), [np.sqrt(c[x] * np.conj(c[x])) for x in range(len(c))])
# plt.xlim(-1, 50)
# plt.show()


# First ten percent of coefficients
#
# tenPercent = len(c) * 0.10
#
# c = [c[x] * (1 if x <= tenPercent else 0) for x in range(len(c))]
#
# inverse = fft.irfft(c)
#
# plt.plot(range(len(df.index)), df.iloc[:, 0])
# plt.plot(range(len(inverse)), inverse)
# plt.show()


# First two percent of coefficients

twoPercent = len(c) * 0.02

c = [c[x] * (1 if x <= twoPercent else 0) for x in range(len(c))]

inverse = fft.irfft(c)

plt.plot(range(len(df.index)), df.iloc[:, 0])
plt.plot(range(len(inverse)), inverse)
plt.show()
