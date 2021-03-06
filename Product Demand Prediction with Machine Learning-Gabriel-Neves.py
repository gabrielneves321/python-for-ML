# -*- coding: utf-8 -*-
"""Untitled64.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TLLUJf8zzyL5RZfd_XLpCUgMGu68FF13
"""

import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("/content/product.csv")
data.head()
print(data)

data.isnull().sum()

data = data.dropna()

data.head()

print(data)

fig = px.scatter(data,x="Units Sold",y="Total Price",size="Units Sold")
fig.show()

print(data.corr())

correlations = data.corr(method='pearson')
plt.figure(figsize=(8,6))
sns.heatmap(correlations,cmap="coolwarm",annot=True)
plt.show()

x = data[["Total Price", "Base Price"]]
y = data["Units Sold"]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)

#features = [["Total Price", "Base Price"]]
features = np.array([[133.00,140.00]])
model.predict(features)

model.score(xtest,ytest)