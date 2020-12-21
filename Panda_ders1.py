# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:07:31 2020

@author: Baran
"""

import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo =pd.read_csv(url,sep="\t") # Seperator olarak tab kullandığımız anlamına geliyor ! ! !
chipo.head()

#print(chipo.head(10)) # ilk on veriyi gösteriyor

print(chipo.shape) # burdan satır ve sutun sayısını bulabiliyoruz.
print(chipo.shape[0]) # burdan kaç satırlık eğitim olduğu bulunuyor ! ! ! 
print(chipo.info()) # burdan özellikler çıkıyor ! ! !

print(chipo.shape[1]) # burdan kaç sütün olduğu bulunuyor ! ! ! 
print(len(chipo.columns)) # veya böylede sütün sayısı elde edilebliyor ! ! 

print(chipo.columns) # sütün adları elde ediliyor

print(chipo.index) # nasıl indexlendiği anlatılıyor 

print(chipo.groupby(by="item_name").sum().sort_values(by="quantity",ascending=False).head(1))
# en çok sipariş edileni bulup onu yazdırıyor ! !

print(chipo.groupby(by="choice_description").sum().sort_values(by="quantity",ascending=False).head(1))

print(chipo.quantity.sum())# toplamda sipariş edilen ürün sayısı

# chipo["item_price].dtype bize item price'ın data tipini verecektir

print(chipo["item_price"][1])

a=float(chipo["item_price"][1][1:-1]) # Bu sayede object sınıfından gelen veriyi float'a çevirmiş oluyoruz

print(a)


floatize = lambda x: float(x[1:-1])
chipo["item_price"] = chipo["item_price"].apply(floatize)

print(chipo["item_price"].dtype)

print((chipo["quantity"]*chipo["item_price"]).sum())

chipo["revenue"] = chipo["quantity"]*chipo["item_price"]

print(chipo.groupby(by="order_id").sum().mean()["revenue"])

print(chipo.item_name.value_counts().count())














