# -*- coding: utf-8 -*-
"""Engineering Placements Prediction using Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qLVfMwN7VcNMusQU7J_NARRZOwgHGOeb
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('collegePlace.csv')

df.head()

df.shape

df.info()

df.isna().sum()

df.Stream.unique()

plt.xticks(rotation = 90)
sns.barplot(x = df.Stream, y = df.PlacedOrNot)

df.Age.unique()

plt.figure(figsize = (12,7))
sns.barplot(x = df.Age, y = df.PlacedOrNot, hue = df.Gender)

plt.figure(figsize = (7,5))
sns.countplot(x = df.Age)

df.Age.value_counts()

sns.barplot(x = df.Internships, y = df.PlacedOrNot)

df.Internships.value_counts()

df.CGPA.value_counts()

sns.barplot(x = df.CGPA, y = df.PlacedOrNot)

sns.barplot(x = df.Hostel, y = df.PlacedOrNot)

sns.barplot(x = df.Gender, y = df.PlacedOrNot)

sns.barplot(x = df.HistoryOfBacklogs, y = df.PlacedOrNot)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df.Gender = le.fit_transform(df.Gender)
df.Stream = le.fit_transform(df.Stream)

df.head()

x = df.drop(['PlacedOrNot'], axis = 1)

y = df.PlacedOrNot

from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import cross_val_score

cross_val_score(SVC(),x, y, cv = 3)

cross_val_score(DecisionTreeClassifier(), x, y, cv = 3)

cross_val_score(LogisticRegression(), x, y, cv = 3)

cross_val_score(RandomForestClassifier(n_estimators=50), x, y, cv = 3)

cross_val_score(KNeighborsClassifier(),x, y ,cv = 3)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot = True)

print("Training Accuracy :", model.score(X_train, y_train))
print("Testing Accuracy :", model.score(X_test, y_test))