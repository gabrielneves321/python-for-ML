# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jSrsQvDT28XJMtkzRPSMMf5cXiar7bg_
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/record.csv')
df.plot()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/record.csv')
df.plot(kind = 'scatter',x='Marks',y='total')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/record.csv')
df.plot(kind = 'scatter',x='Percentage',y='total')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/record.csv')
df.plot(kind = 'scatter',x='Percentage',y='Marks')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/record.csv')
df["Marks"].plot(kind = 'hist')