# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:38:08 2020

@author: Baran
"""

import pandas as pd
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
user_id = pd.read_csv(url,sep="|")
print(user_id.head(25))

print(user_id.tail(10)) # en sondan 10 elemanı gösteriyor 

print(user_id.columns)

print(user_id.shape[0]) # kaç gözlem olduğu belirtiliyor ! ! 
print(user_id.shape[1]) # kaç özellik olduğu bulunuyor ! 

print(user_id.index) # Veri setinin nasıl indexlendiğini gösteriyor ! ! !

#print(user_id.dtype) # Veri tiplerinin neler olduğunu görebiliyoruz ! 
#print(user_id["occupation"].dtype)

print(user_id["occupation"])

print(user_id["occupation"].nunique()) # Kaç tane farklı değer var
print(user_id["occupation"].value_counts().count())  # Kaç tane farklı değer var

# Summarize Dataset

print(user_id.describe())

print(user_id.describe(include="all")) #obje değişkenlerede aynı işlemleri yapmaya çalışıyor

print(user_id["occupation"].describe())

print(user_id["age"].mean()) # Kullanıcıların yaş ortalaması

