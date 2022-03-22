import numpy as np
import numpy.fft as fft
import cmath as cm
import pandas as pd
import matplotlib.pyplot as plt

samples = range(0, 1000)

square_wave = [np.sign(np.sin(x / 106)) for x in samples]
sw_ftt = fft.irfft(fft.rfft(square_wave))

saw_tooth = [(x / 500) - 1 for x in samples]
st_ftt = fft.irfft(fft.rfft(saw_tooth))

mod_sin = [np.sin(np.pi * x / 1000) * np.sin(20 * np.pi * x / 1000) for x in samples]
ms_ftt = fft.irfft(fft.rfft(mod_sin))

print(st_ftt[999])

plt.plot(samples, sw_ftt)
plt.plot(samples, st_ftt)
plt.plot(samples, ms_ftt)
plt.show()