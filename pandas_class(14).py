# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19w2EyA_SR87cosO_rPukWN3kFy6W4Zrb
"""

import pandas as pd
df=pd.read_csv('/content/data.csv')
df.fillna("Gaud", inplace=True)
print(df)

import pandas as pd
df=pd.read_csv('/content/data.csv')
df["LastName"].fillna("Gaud", inplace = True)
print(df)

import pandas as pd
df=pd.read_csv('/content/data.csv')
x=df["scholor number"].mean()
df["scholor number"].fillna(x,inplace=True)
print(df)

import pandas as pd
df=pd.read_csv('/content/data.csv')
x=df["scholor number"].median()
df["scholor number"].fillna(x,inplace=True)
print(df)

import pandas as pd
df=pd.read_csv('/content/data.csv')
x=df["scholor number"].mode()[0]
df["scholor number"].fillna(x,inplace=True)
print(df)
