#from scipy.fft import fft, ifft
from scipy import fft
from scipy.fftpack import fft,ifft
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
#plt.plot(real(y))
print(y)
