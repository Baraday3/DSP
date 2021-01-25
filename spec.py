# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:01:53 2021

@author: Baran
"""

from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import chirp
import scipy.io as sio
import h5py
test = sio.loadmat('test_1.mat')

asd=test['Vr'][0,]

tst=asd




i=1j
N=2 #Number of Blades
L=5# Pervane Boyu
v=0# helicopter velocity
fc = 9.5e9# radar carrier frequency
c = 2.99792458e8
lambdaa = c/fc
beta = 10
beta = beta*np.pi/180
fr = 4 # Rotation Rate
R = 100 # Radar Range
samplerate = 60000
dt = 1/samplerate
Sigma = 1
NSample = 60000
F = 1/dt
T = NSample*dt
VR=[]
times=[]
Vtip = L*fr*2*np.pi;
print(Vtip) # in (m/s)
Max_Doppler_Frequency=(np.cos(beta)*2*fc*Vtip/c)/1000 # in KHz
print(Max_Doppler_Frequency)


plt.figure(0)
plt.plot(abs(tst))

plt.figure(1)
VR_FFT=abs(np.fft.fftshift(np.fft.fft(tst)))
frekanslar=np.arange(-F/2,(F/2)-(F/NSample-1),F/NSample)
plt.plot(frekanslar,VR_FFT)

plt.figure(3) 
ptt,ftt,ttt,rst = plt.specgram(tst, NFFT=512, Fs=F, noverlap=400,sides='twosided')



print(" Spectrogram Feature Extraction")


index=255
index_2=511

saniyeler=[]

for sad in range(0,512): 
    enbuyuk =10*np.log10(ptt[511,sad])
    index=255
    index_2=511
    while(index>0):
        if(enbuyuk+10<10*np.log10(ptt[256+index,sad])):
            enbuyuk=10*np.log10(ptt[256+index,sad])
            index_2=index
       
        index=index-1
    saniyeler.append(ftt[256+index_2])


# print(saniyeler) 
maksimum_Frekans=max(saniyeler)
maksimum_Frekans_Indexes= []

for sad in range (0,512):
    if(maksimum_Frekans==saniyeler[sad]):
        maksimum_Frekans_Indexes.append(sad)


filtered_maksimum_Frekans_Indexes=[maksimum_Frekans_Indexes[0]]
lenghtOfFrekansIndexes=len(maksimum_Frekans_Indexes)

sad_1 = 0


for sad in range (0,lenghtOfFrekansIndexes):
   
    if((maksimum_Frekans_Indexes[sad]) > filtered_maksimum_Frekans_Indexes[sad_1]+10):
        
        filtered_maksimum_Frekans_Indexes.append(maksimum_Frekans_Indexes[sad])
        sad_1=sad_1+1

Period=ttt[filtered_maksimum_Frekans_Indexes[1]-filtered_maksimum_Frekans_Indexes[0]]


print("Sinyalin Frekansı : " +str(maksimum_Frekans))
print("Sinyalin Periyodu : "+str(Period))





