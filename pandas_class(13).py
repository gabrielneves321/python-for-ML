# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YrbCJWMYURGEc3EoQwz5r6E-18kxN9SI
"""

import pandas as pd
df = pd.read_json('/iris.json')
print(df)
print(df.to_string()) #console friendly tabular format

import pandas as pd

data={
  "sepalLength":{
  "0":0.60,
  "1":0.60,
  "2":0.60,
  "3":0.45,
  "4":0.45,
  "5":0.60
  },
  "sepalWidth":{
  "0":0.110,
  "1":0.117,
  "2":0.103,
  "3":0.109,
  "4":0.117,
  "5":0.102
 },
  "petalLength":{
  "0":0.130,
  "1":0.145,
  "2":0.135,
  "3":0.175,
  "4":0.148,
  "5":0.127
  },
  "petalWidth":{
  "0":0.409,
  "1":0.479,
  "2":0.340,
  "3":0.282,
  "4":0.406,
  "5":0.300
}
}
df=pd.DataFrame(data)
print(df)

import pandas as pd
df = pd.read_csv('/data.csv')
new_df = df.dropna()
print(new_df.to_string())
print(df.to_string())

import pandas as pd
df = pd.read_csv('/data.csv')
df.dropna(inplace=True)
print(df.to_string())

import pandas as pd
df = pd.read_csv('/data.csv')
print(df.to_string())
df.dropna(inplace=True)
print(df.to_string())