# -*- coding: utf-8 -*-
"""Untitled90.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10jNONUXfyCbDQCR811HWkiUi_LKZeAP5
"""

import pandas as pd
scores = [['Mathematics', 85, 'Science'],
['English', 91, 'Arts'],
['History', 95, 'Chemistry'],
['History', 95, 'Chemistry'],
['English', 95, 'Chemistry'],
]
my_df = pd.DataFrame(scores, columns = ['Subject', 'Score', 'Subject'])
my_df.head()

result = my_df.drop_duplicates()
result.head()

print(my_df)

result = my_df.drop_duplicates(keep='first')
result.head()

result = my_df.drop_duplicates(keep=False)
result.head()

result = my_df.drop_duplicates(subset=['Score'])
result.head()

import pandas as pd
scores = [['Mathematics', 85, 'Science', 85],
['English', 91, 'Arts', 91],
['History', 95, 'Chemistry', 95],
['History', 95, 'Chemistry', 95],
['English', 95, 'Chemistry', 95],
]
my_df = pd.DataFrame(scores, columns = ['Subject', 'Score', 'Subject',
'Percentage'])
my_df.head()

result = my_df.loc[:,~my_df.columns.duplicated()]
result.head()

result = my_df.T.drop_duplicates().T
result.head()

scores = pd.DataFrame({'name':['Adam', 'Bob', 'Dave', 'Fred'],
'age': [15, 16, 16, 15],
'test1': [95, 81, 89, None],
'test2': [80, 82, 84, 88],
'teacher': ['Ashby', 'Ashby', 'Jones', 'Jones']})
scores

scores.pivot_table(index='teacher',
   values=['test1', 'test2'],
   aggfunc='median')

scores.pivot_table(index=['teacher', 'age'],
values=['test1', 'test2'],
aggfunc='median')

scores.pivot_table(index='teacher',
                  values=['test1', 'test2'],
                   aggfunc=[min, max])

scores.pivot_table(index='teacher',
                   values=['test1', 'test2'],
                   aggfunc='median', margins=True)