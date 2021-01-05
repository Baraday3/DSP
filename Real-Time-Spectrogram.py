import random
from itertools import count
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.signal import chirp,spectrogram

Fs = 5000
T = 25
t = np.linspace(0, T, T*Fs, endpoint=False)
NFFT=512
index = count()
def animate(i):
    w = chirp(t, f0=500+np.random.randint(250), f1=100+np.random.randint(150), t1=np.random.randint(1,10), method='linear')
    w1 = chirp(t, f0=700+np.random.randint(250), f1=400+np.random.randint(150), t1=np.random.randint(1,10), method='linear')
    w2 = chirp(t, f0=500+np.random.randint(250), f1=100+np.random.randint(150), t1=np.random.randint(1,10), method='linear')
    s1 = 2*np.sin(2 * np.pi * (np.random.randint(25)*100+np.random.randint(150)) * t)
    s2 = 2 * np.sin(2 * np.pi * (np.random.randint(6)*400+np.random.randint(250)) * t)
    s2[t <= random.randint(1, 9)] = s2[random.randint(10, 25) <= t] = 0
    s3 = 2 * np.sin(2 * np.pi * (np.random.randint(6)*300+np.random.randint(250)) * t)
    s3[t <= random.randint(1, 9)] = s3[random.randint(10, 25) <= t] = 0
    nse = (np.random.randint(50)/100) * np.random.random(size=len(t))
    z=w+s1+s2+nse+w1+s3+w2
    plt.clf()

    plt.xlabel('Zaman (Saniye)')
    plt.ylabel('Frekans (Hz))')
    ptt,ftt,ttt,rst = plt.specgram(z, NFFT=NFFT, Fs=Fs, noverlap=450)
    print(ttt.max())




ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.show()
