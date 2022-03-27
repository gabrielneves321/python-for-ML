# -*- coding: utf-8 -*-
"""Untitled87.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ywPFinJ1UYathcyrBB5zI-YKdc7alP3u
"""

import pandas as pd
scores = [
{'Subject':'Mathematics', 'Score':85, 'Grade': 'B', 'Remarks': 'Good',
},
{'Subject':'History', 'Score':98, 'Grade': 'A','Remarks':
'Excellent'},
{'Subject':'English', 'Score':76, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'Science', 'Score':72, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'Arts', 'Score':95, 'Grade': 'A','Remarks': 'Excellent'},
]
my_df = pd.DataFrame(scores)
my_df.head()

my_df2 = my_df.drop(["Grade","Remarks"], axis=1)
my_df2

my_df.drop(["Subject", "Grade"], axis = 1, inplace = True)
my_df.head()

my_df2 = my_df.filter([1,3,4],axis=0)
my_df2

my_df2 = my_df2.reset_index(drop=True)
my_df2.head()

my_df2 = my_df.filter(["Score","Grade"],axis=1)
my_df2.head()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
titanic_data = sns.load_dataset('titanic')
titanic_data.head()

age_sorted_data = titanic_data.sort_values(by=['age'])
age_sorted_data.head()

age_sorted_data = titanic_data.sort_values(by=['age'], ascending=False)
age_sorted_data.head()

age_sorted_data = titanic_data.sort_values(by=['age','fare'], ascending=False)
age_sorted_data.head()