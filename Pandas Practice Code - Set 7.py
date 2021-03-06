# -*- coding: utf-8 -*-
"""Untitled85.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PDciCqOOu4PCbQkN-B--e-nq5oxTbyD-
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

my_df.iloc[3]

my_df.iloc[[2,3,4]]

my_df.iloc[2:4]

my_df.iloc[[2,3],[0,1]]

my_df.iloc[2:4,0:2]

my_df2 = my_df.drop([1,4])
my_df2.head()

my_df2.reset_index(inplace=True)
my_df2.head()

my_df2 = my_df.drop([1,4])
my_df2.head()

my_df2.reset_index(inplace=True, drop = True)
my_df2.head()

my_df.drop([1,3,4])
my_df.head()

my_df.drop([1,3,4], inplace=True)
my_df.head()