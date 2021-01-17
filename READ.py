import numpy as np
import pandas as pd
import pickle
import socket

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression




#   HDR + DSP_Header +DSP_Data = 8 + 8 + 140 = 156 Byte

#   HDR = HDR.Sign(4) + HDR.Size(4)



buffer=""
HDR_Sign=np.str("")
HDR_Size=np.int32(0)
DSP_Header=""


prf=np.int32(0)
pdr=np.int32(0)
sft=np.int32(0)
avc=np.int32(0)
ihp=np.int32(0)
chg=np.int32(0)
gbw=np.int32(0)

dell=np.int32(0)
dur=np.int32(0)

res0=np.float(0)
res1=np.float(0)







a=np.byte()




f=open("raw.txt","rb")
d=f.read()




HDR_Size=d[4]
HDR_Size=HDR_Size*256+d[6]
HDR_Size=HDR_Size*256+d[7]
HDR_Size=HDR_Size*256+d[8]





print (HDR_Size)

e=chr(d[0])
b=chr(d[1])
c=chr(d[2])
d=chr(d[3])

HDR_Sign= e+b+c+d
print (HDR_Sign)