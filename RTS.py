import random
from itertools import count
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.signal import chirp,spectrogram

Fs = 5000
T = 15
t = np.linspace(0, T, T*Fs, endpoint=False)
t2 = np.linspace(0.9, T+0.9, T*Fs, endpoint=False)
NFFT=512
fig, axs = plt.subplots(3)

index = count()
def animate(i):
    w = 25*chirp(t, f0=500,f1=200 , t1=0.1, method='linear') + 25*chirp(t2, f0=500,f1=200 , t1=0.1, method='linear',)
    
    nse = (np.random.randint(500)/100) * np.random.random(size=len(t))
    z=w+nse
    plt.clf()
    

    plt.xlabel('Zaman (Saniye)')

    plt.ylabel('Frekans (Hz))')
    plt.title('Tek Sayılı Pervanelere Ait Dron Çıktısı')
    ptt,ftt,ttt,rst = plt.specgram(z, NFFT=NFFT, Fs=Fs, noverlap=450)
    ptt = 20*np.log10(ptt)
    print(ptt.max())
    print(ftt.max())




ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.show()
