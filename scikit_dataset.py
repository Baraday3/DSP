# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:01:13 2020

@author: Baran
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# clf = RandomForestClassifier(random_state=0)
# X = [[ 1,  2,  3],[11, 12, 13]]

# y = [0, 1]  # classes of each sample
# clf.fit(X, y)
# a=clf.predict(X)
# print(a)

x=[[25.1,10],[-12.3,45],[6.5,70],[30.7,12],[-4.8,33],[8.9,65],[1.5,15],[4.1,10]]
y=[0,3,2,0,3,2,1,1]

clf = RandomForestClassifier(random_state=0)

clf.fit(x,y)

x1=[[20,7],[-1,4]]
y1=[0,3]

c= clf.predict(x1)
print(c)


a=accuracy_score(clf.predict(x1),y1)

print(a)