# -*- coding: utf-8 -*-
"""Untitled77.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vKlj07G1YLi2yrQj7p0OAfAY05a7JW4U
"""

import pandas as pd
titanic_data = pd.read_csv('/content/titanic.csv')
titanic_data.head()

import pandas as pd
titanic_data = pd.read_csv('/content/titanic.csv')
titanic_data.tail()

import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = [8,6]
sns.set_style("darkgrid")
titanic_data = sns.load_dataset('titanic')
titanic_data.head()

titanic_data = titanic_data[["survived", "pclass", "age", "fare"]]
titanic_data.head()

titanic_data.isnull().mean()

median = titanic_data.age.median()
print(median)
mean = titanic_data.age.mean()
print(mean)

import numpy as np
titanic_data['Median_Age'] = titanic_data.age.fillna(median)
titanic_data['Mean_Age'] = titanic_data.age.fillna(mean)
titanic_data['Mean_Age'] = np.round(titanic_data['Mean_Age'], 1)
titanic_data.head(20)

fig = plt.figure()
ax = fig.add_subplot(111)
titanic_data['age'] .plot(kind='kde', ax=ax)
titanic_data['Median_Age'] .plot(kind='kde', ax=ax, color='red')
titanic_data['Mean_Age'] .plot(kind='kde', ax=ax, color='green')
lines, labels = ax.get_legend_handles_labels()
ax.legend(lines, labels, loc='best')
