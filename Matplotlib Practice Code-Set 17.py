# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10aNHyp6JJ-ktYYQM-4zhKNZbdCsFwbJy
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 4),
columns=['A', 'B', 'C', 'D'])
print(df)
plt.figure()
df.plot.area()
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 4),
columns=['A', 'B', 'C', 'D'])
plt.figure()
df.plot.area(stacked=False)
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 4),
columns=['A', 'B', 'C', 'D'])
print(df)
plt.figure()
df.plot.scatter(x='A', y='B')
plt.show()

df = pd.DataFrame(np.random.rand(10, 4),
                 columns=['A', 'B', 'C', 'D'])
print(df)
ax = df.plot.scatter(x='A', y='B',
                    color='Blue',
                    label='Group 1')
plt.figure()
df.plot.scatter(x='C', y='D',
               color='Green',
               label='Group 2',
               ax=ax)
plt.show()

df = pd.DataFrame(np.random.rand(10, 4),
columns=['A', 'B', 'C', 'D'])
print(df)
plt.figure()
df.plot.scatter(x='A', y='B', c='C', s=40)
plt.show()

df = pd.DataFrame(np.random.rand(10, 4),
columns=['A', 'B', 'C', 'D'])
print(df)
plt.figure()
df.plot.scatter(x='A', y='B', s=df['C']*100)
plt.show()

df = pd.DataFrame(np.random.rand(10, 4),
columns=['A', 'B', 'C', 'D'])
print(df)
plt.figure()
df.plot.scatter(x='A', y='B', c='C', s=df['D']*100)
plt.show()

df = pd.DataFrame(np.random.randn(100, 2),
columns=['A', 'B'])
df['B'] = df['B'] + np.arange(100)
print(df)
plt.figure()
df.plot.hexbin(x='A', y='B', gridsize=20)
plt.show()