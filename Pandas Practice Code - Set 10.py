# -*- coding: utf-8 -*-
"""Untitled89.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IjwZIewv-JhbgGW7HV6W4gtZPrNDhPQt
"""

import matplotlib.pyplot as plt
import seaborn as sns
titanic_data = sns.load_dataset('titanic')
titanic_data.head()

titanic_pclass1_data = titanic_data[titanic_data["class"] == "Fisrt"]
print(titanic_pclass1_data.shape)
titanic_pclass2_data = titanic_data[titanic_data["class"] == "Second"]
print(titanic_pclass2_data.shape)

final_data = titanic_pclass1_data.append(titanic_pclass2_data,ignore_index=True)
print(final_data.shape)

import pandas as pd
df1 = final_data[:200]
print(df1.shape)
df2 = final_data[200:]
print(df2.shape)
final_data2 = pd.concat([df1,df2],axis=1,ignore_index=True)
print(final_data2.shape)

import pandas as pd
scores1 = [
{'Subject':'Mathematics', 'Score':85, 'Grade': 'B', 'Remarks': 'Good',
},
{'Subject':'History', 'Score':98, 'Grade': 'A','Remarks':
'Excellent'},
{'Subject':'English', 'Score':76, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'Chemistry', 'Score':72, 'Grade': 'C','Remarks': 'Fair'},
]
scores2 = [
{'Subject':'Arts', 'Score':70, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'Physics', 'Score':75, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'English', 'Score':92, 'Grade': 'A','Remarks':
'Excellent'},
{'Subject':'Chemistry', 'Score':91, 'Grade': 'A','Remarks':
'Excellent'},
]
scores1_df = pd.DataFrame(scores1)
scores2_df = pd.DataFrame(scores2)

scores1_df.head()

scores2_df.head()

join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='inner')
join_inner_df.head()

join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='left')
join_inner_df.head()

join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='right')
join_inner_df.head()

join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='outer')
join_inner_df.head()