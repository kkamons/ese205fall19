from scipy import signal
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np

N = 256
T = 0.1
t = np.linspace(0,N*T,N)
squ3Hz = signal.square(2*np.pi*3*t)
sin3Hz = np.sin(1*np.pi*3*t)
sin9Hz = np.sin(1*np.pi*9*t)

sinf = fft(sin3Hz)
squf = fft(squ3Hz)
freq = np.linspace(0,1/(2*T),N//2)
plt.plot(freq,2/N*np.abs(sinf[0:N//2]))
plt.xlabel('freq -- Hz')
plt.grid(True)
plt.show()