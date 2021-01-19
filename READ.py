import numpy as np
import pandas as pd
import pickle
import socket
import sys
import matplotlib.pyplot as plt
import scipy.signal as signal

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression


###### TCP/IP Communication Initials 

TCP_IP = '192.168.1.4'
TCP_PORT = 8888
BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


I=np.array[0]
Q=np.array[0]




#   HDR + DSP_Header +DSP_Data = 8 + 8 + 140 = 156 Byte

#   HDR = HDR.Sign(4) + HDR.Size(4)



buffer=""
HDR_Sign=np.str("")
HDR_Size=np.int32(0)
DSP_Header=""


prf=np.int32(0)                 #    Now it is not index, but just integer value
pdr=np.int32(0)                 #    Pulse Duration in ns
sft=np.int32(0)                 #    FFT Length in Samples
avc=np.int32(0)                 #    Count of FFT in Average   
ihp=np.int32(0)                 #    Initial Height Gate (Starting from 0 gate, having Zero Distance)
chg=np.int32(0)                 #    Count of Height Gates     
gbw=np.int32(0)                 #    Gate Bin Width in ns (instead of polarization)
dell=np.int32(0)                #    ADC Delay  (msc)
dur=np.int32(0)                 #    Pulse Duration (msc)
res0=np.float(0)                #    Reserved
res1=np.float(0)                #    Reserved
dbg=np.int32(0)                 #    Debug Options
pos=np.int32(0)                 #    Pulse Position for Ph.Corr (tcn)
add=np.int32(0)                 #    Addition to Pulse Length is ns (tcn)
lenn=np.int32(0)                #    Reserved (tcn)
cal=np.int32(0)                 #    Calibration Signal Offset in ns (tcn)
ubx=np.int32(0)                 #    Extended (Predefined) Modes. WAS: "Noise Position Offset in ns" (tcn)
nth=np.int32(0)                 #    Noise Threshold (msc)
ppow=np.int32(0)                #    Pulse Power, rel.un., 15....31 (msc)
att=np.int32(0)                 #    Receiver Attenuation, dB, 0....31 (msc)
summ=np.int32(0)                #    Bool: "Averaging Along Pulse" (opt)
osc=np.int32(0)                 #    Bool: "Oscilloscope Mode" (opt)
tst=np.int32(0)                 #    Bool: "Test Mode" (opt)
cor=np.int32(0)                 #    Bool: "Phase Correction" (opt)
dco=np.int32(0)                 #    Bool: "DC Compensation" (opt)
hsn=np.int32(0)                 #    Bool: "HS on Noise Gates" (opt)
hsa=np.int32(0)                 #    Bool: "HS on All Gates" (opt)
CalibrPower_M=np.float(0)       #    Float Out
CalibrSNR_M=np.float(0)         #    Float Out
CalibrPower_S=np.float(0)       #    Float Out
CalibrSNR_S=np.float(0)         #    Float Out
Raw_Gate1=np.int32(0)           #    
Raw_Gate2=np.int32(0)           #    
Raw=np.int32(0)                 #    0-NONE, 1-FFT, 2-OSC
Prc=np.int32(0)                 #    0-NONE, 1-Moments


frm=np.str("")                  #    Data Frame 2^32-1
Tm=np.str("")                   #    Time of Data Frame
TPow=np.float(0)                #    Transmitter Power
NPw1=np.float(0)                #    Receiver 1 Noise Power
NPw2=np.float(0)                #    Receiver 2 Noise Power
CPw1=np.float(0)                #    Receiver 1 Calibration Power
CPw2=np.float(0)                #    Receiver 2 Calibration Power
PS_err=np.str("")               #    Power Supply Error
RC_err=np.str("")               #    Receiver Error
TR_err=np.str("")               #    Transmitter Error
dwSTAT=np.str("")               #    System Global State
dwGRST=np.str("")               #    System Global Status
AzmPos=np.float(0)              #    
ElvPos=np.float(0)              #    
AzmVel=np.float(0)              #    
ElvVel=np.float(0)              #    
NorthP=np.float(0)              #    North Direction
tv_us=np.str("")                #    Set Azimuth Position
res1=np.str("")                 #    Set Elevation Position
res2=np.str("")                 #    Set Azimuth Velocity
res3=np.str("")                 #    Set Elevation Velocity

a=np.byte()




    # f=open("raw.txt","rb")
    # d=f.read()


while 1:
    d = s.recv(BUFFER_SIZE)
    # s.send(MESSAGE)

    HDR_Size=d[4]
    HDR_Size=HDR_Size*256+d[5]
    HDR_Size=HDR_Size*256+d[6]
    HDR_Size=HDR_Size*256+d[7]
    
    prf=d[8]
    prf=prf*256+d[9]
    prf=prf*256+d[10]
    prf=prf*256+d[11]
    
    pdr=d[12]
    pdr=pdr*256+d[13]
    pdr=pdr*256+d[14]
    pdr=pdr*256+d[15]
    
    sft=d[16]
    sft=sft*256+d[17]
    sft=sft*256+d[18]
    sft=sft*256+d[19]
    
    avc=d[20]
    avc=avc*256+d[21]
    sft=avc*256+d[22]
    avc=avc*256+d[23]
    
    ihp=d[24]
    ihp=ihp*256+d[25]
    ihp=ihp*256+d[26]
    ihp=ihp*256+d[27]
    
    chg=d[28]
    chg=chg*256+d[29]
    chg=chg*256+d[30]
    chg=chg*256+d[31]
    
    gbw=d[32]
    gbw=gbw*256+d[33]
    gbw=gbw*256+d[34]
    gbw=gbw*256+d[35]
    
    dell=d[36]
    dell=dell*256+d[37]
    dell=dell*256+d[38]
    dell=dell*256+d[39]
    
    dur=d[40]
    dur=dur*256+d[41]
    dur=dur*256+d[42]
    dur=dur*256+d[43]
    
    res0=d[44]
    res0=res0*256+d[45]
    res0=res0*256+d[46]
    res0=res0*256+d[47]
    
    res1=d[48]
    res1=res1*256+d[49]
    res1=res1*256+d[50]
    res1=res1*256+d[51]
    
    dbg=d[52]
    dbg=dbg*256+d[53]
    dbg=dbg*256+d[54]
    dbg=dbg*256+d[55]
    
    pos=d[56]
    pos=pos*256+d[57]
    pos=pos*256+d[58]
    pos=pos*256+d[59]
    
    add=d[60]
    add=add*256+d[61]
    add=add*256+d[62]
    add=add*256+d[63]
    
    lenn=d[64]
    lenn=lenn*256+d[65]
    lenn=lenn*256+d[66]
    lenn=lenn*256+d[67]
    
    cal=d[68]
    cal=cal*256+d[69]
    cal=cal*256+d[70]
    cal=cal*256+d[71]
    
    ubx=d[72]
    ubx=ubx*256+d[73]
    ubx=ubx*256+d[74]
    ubx=ubx*256+d[75]
    
    nth=d[76]
    nth=nth*256+d[77]
    nth=nth*256+d[78]
    nth=nth*256+d[79]
    
    ppow=d[80]
    ppow=ppow*256+d[81]
    ppow=ppow*256+d[82]
    ppow=ppow*256+d[83]
    
    att=d[84]
    att=att*256+d[85]
    att=att*256+d[86]
    att=att*256+d[87]
    
    summ=d[88]
    summ=summ*256+d[89]
    summ=summ*256+d[90]
    summ=summ*256+d[91]
    
    osc=d[92]
    osc=osc*256+d[93]
    osc=osc*256+d[94]
    osc=osc*256+d[95]
    
    tst=d[96]
    tst=tst*256+d[97]
    tst=tst*256+d[98]
    tst=tst*256+d[99]
    
    cor=d[100]
    cor=cor*256+d[101]
    cor=cor*256+d[102]
    cor=cor*256+d[103]
    
    dco=d[104]
    dco=dco*256+d[105]
    dco=dco*256+d[106]
    dco=dco*256+d[107]
    
    hsn=d[108]
    hsn=hsn*256+d[109]
    hsn=hsn*256+d[110]
    hsn=hsn*256+d[111]
    
    hsa=d[112]
    hsa=hsa*256+d[113]
    hsa=hsa*256+d[114]
    hsa=hsa*256+d[115]
    
    CalibrPower_M=d[116]
    CalibrPower_M=CalibrPower_M*256+d[117]
    CalibrPower_M=CalibrPower_M*256+d[118]
    CalibrPower_M=CalibrPower_M*256+d[119]
    
    CalibrSNR_M=d[120]
    CalibrSNR_M=CalibrSNR_M*256+d[121]
    CalibrSNR_M=CalibrSNR_M*256+d[122]
    CalibrSNR_M=CalibrSNR_M*256+d[123]
    
    CalibrPower_S=d[124]
    CalibrPower_S=CalibrPower_S*256+d[125]
    CalibrPower_S=CalibrPower_S*256+d[126]
    CalibrPower_S=CalibrPower_S*256+d[127]
    
    CalibrSNR_S=d[128]
    CalibrSNR_S=CalibrSNR_S*256+d[129]
    CalibrSNR_S=CalibrSNR_S*256+d[130]
    CalibrSNR_S=CalibrSNR_S*256+d[131]
    
    Raw_Gate1=d[132]
    Raw_Gate1=Raw_Gate1*256+d[133]
    Raw_Gate1=Raw_Gate1*256+d[134]
    Raw_Gate1=Raw_Gate1*256+d[135]
    
    Raw_Gate2=d[136]
    Raw_Gate2=Raw_Gate2*256+d[137]
    Raw_Gate2=Raw_Gate2*256+d[138]
    Raw_Gate2=Raw_Gate2*256+d[139]
    
    Raw=d[140]
    Raw=Raw*256+d[141]
    Raw=Raw*256+d[142]
    Raw=Raw*256+d[143]
    
    Prc=d[144]
    Prc=Prc*256+d[145]
    Prc=Prc*256+d[146]
    Prc=Prc*256+d[147]
    
    #SVRIT Data'ları 8 Byte sonra başlıyor
    
    TPow=d[163]
    TPow=TPow*256+d[164]
    TPow=TPow*256+d[165]
    TPow=TPow*256+d[166]
    
    NPw1=d[167]
    NPw1=NPw1*256+d[168]
    NPw1=NPw1*256+d[169]
    NPw1=NPw1*256+d[170]
    
    NPw2=d[171]
    NPw2=NPw2*256+d[172]
    NPw2=NPw2*256+d[173]
    NPw2=NPw2*256+d[174]
    
    CPw1=d[175]
    CPw1=CPw1*256+d[176]
    CPw1=CPw1*256+d[177]
    CPw1=CPw1*256+d[178]
    
    CPw2=d[179]
    CPw2=CPw2*256+d[180]
    CPw2=CPw2*256+d[181]
    CPw2=CPw2*256+d[182]
    
    AzmPos=d[203]
    AzmPos=AzmPos*256+d[204]
    AzmPos=AzmPos*256+d[205]
    AzmPos=AzmPos*256+d[206]
    
    AzmVel=d[207]
    AzmVel=AzmVel*256+d[208]
    AzmVel=AzmVel*256+d[209]
    AzmVel=AzmVel*256+d[210]
    
    ElvPos=d[211]
    ElvPos=ElvPos*256+d[212]
    ElvPos=ElvPos*256+d[213]
    ElvPos=ElvPos*256+d[214]
    
    ElvVel=d[215]
    ElvVel=ElvVel*256+d[216]
    ElvVel=ElvVel*256+d[217]
    ElvVel=ElvVel*256+d[218]
    
    NorthP=d[219]
    NorthP=NorthP*256+d[220]
    NorthP=NorthP*256+d[221]
    NorthP=NorthP*256+d[222]
    
# avc*sft-1'e kadar I ve Q 'yu alacağız. 223
    z_range=range(223,avc*sft-1,1)
    for ity in z_range:
        
        if ity%2==0:
            I=np.append(I,d[ity])
        else:
            Q=np.append(Q,d[ity])

    plt.subplot(411)
    plt.plot(I)
    plt.subplot(412)
    plt.plot(Q)
    combined=I +Q*1j
    plt.plot(np.abs(combined))
    plt.subplot(414)
    plt.specgram(combined,NFFT=2048,Fs=1000)


# print (HDR_Size)

# e=chr(d[0])
# b=chr(d[1])
# c=chr(d[2])
# d=chr(d[3])

# HDR_Sign= e+b+c+d
# print (HDR_Sign)





s.close() # TCP Communication Close