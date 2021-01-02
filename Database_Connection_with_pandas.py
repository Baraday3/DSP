# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Baraday")

import pyodbc 
import pandas as pd

db = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-8B6J9IE\MSSQLSERVER01;'
    'Database=RADAR;'
    'Trusted_Connection=True;'
)
imlec = db.cursor()
imlec.execute('SELECT * FROM Drone_Dataset_Table')
a=imlec.fetchall()
sql="""

SELECT * FROM Drone_Dataset_Table

"""
Dataset =pd.read_sql(sql,db)

print(Dataset["RCS"])
print(Dataset.columns)

# for i in a:
#     print(i)

# Aşağıdaki kod ile veri tabanınıa veri kayıt edilebiliyor ! ! ! ! !
# komut = 'INSERT INTO Drone_Dataset_Table VALUES(?,?,?,?,?,?)'
# veriler = (-1,-1,25,25,25,0)
# sonuc = imlec.execute(komut,veriler)
# db.commit()


# UPDATE İŞLEMİ
# sonuc = imlec.execute('UPDATE Drone_Dataset_Table SET RCS = ? WHERE id = ?',(50,1))
# db.commit()
# print(str(sonuc) + " kullanıcı güncellendi")

#DELETE İŞLEMİ
# sonuc = imlec.execute('DELETE FROM Drone_Dataset_Table WHERE id = ?',(-1.0,))
# db.commit()
# print(str(sonuc) + " kullanıcı silindi")