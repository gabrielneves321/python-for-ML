# -*- coding: utf-8 -*-
"""Untitled40.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Wmd7RRgalvQYB2yPkP1mYTLGifAZ27F
"""

import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('/content/heart.csv')
df.head()

X = df.drop('target',axis=1)
y = df['target']
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7,random_state=42)
X_train.shape,X_test.shape

classifier_rf = RandomForestClassifier(random_state=42,n_jobs=1,max_depth=5,n_estimators=100,oob_score=True).fit(X_train,y_train)

classifier_rf.oob_score_