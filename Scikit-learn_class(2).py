# -*- coding: utf-8 -*-
"""Untitled32.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GJB89HHqiANzBpWcbfjahe3joWYF23mo
"""

import numpy as np
from sklearn import preprocessing

input_data = np.array([[1.,-1.,2.],
                       [2.,0.,0.],
                       [0.,1.,-1.]])

x = [['male','from US','uses Safari'],['female','from Europe','uses Firefox']]

d1 = preprocessing.Binarizer(threshold=0.5).transform(input_data)
d1

input_data.mean(axis=0)

input_data.std(axis=0)

d2 = preprocessing.scale(input_data)
d2

d3 = preprocessing.StandardScaler().fit(input_data)
d3

d3.mean_

print(d3.transform(input_data))

d4 = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(input_data)
d4

d5=preprocessing.normalize(input_data, norm='l1')
d5

0.25+ -0.25+ 0.5

1.+0.+0.

d6=preprocessing.normalize(input_data, norm='l2')
d6

np.sqrt(0.40824829**2 + -0.40824829**2 +0.81649658**2)

x = [['male','from US','uses Safari'],['female','from Europe','uses Firefox']]

d7 = preprocessing.OneHotEncoder().fit(x)
d7 = d7.transform([['female','from US','uses Safari'],['male','from Europe','uses Safari']]).toarray()
d7

d8 = preprocessing.LabelEncoder()
d8.fit(["paris","paris","tokyo","india"])
d8.classes_

d8.transform(["tokyo","tokyo","paris"])
