# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v8uunCR2f9be-NgHwCrp-QcYjRlTxguX
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
labels = ["Chrome","Internet Explorer","Firefox","Edge","Safari","Sogou Explorer","Opera","Others"]
marketshare = [61.64,11.98,11.02,4.23,3.79,1.63,1.52,4.19]
explode = (0,0,0,0,0,0,0,0)
plt.pie(marketshare,
explode = explode,
labels = labels,
autopct="%.1f%%",
shadow=True,
startangle=45)
plt.axis("equal")
plt.title("Web Browser Marketshare - 2021")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
labels = ["Chrome","Internet Explorer","Firefox","Edge","Safari","Sogou Explorer","Opera","Others"]
marketshare = [61.64,11.98,11.02,4.23,3.79,1.63,1.52,4.19]
explode = (0.5,0,0,0,0,0,0.8,0)
plt.pie(marketshare,
explode = explode,
labels = labels,
autopct="%.1f%%",
shadow=True,
startangle=45)
plt.axis("equal")
plt.title("Web Browser Marketshare - 2021")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
labels = ["Chrome","Internet Explorer","Firefox","Edge","Safari","Sogou Explorer","Opera","Others"]
marketshare = [61.64,11.98,11.02,4.23,3.79,1.63,1.52,4.19]
colors = ['yellowgreen','gold','lightskyblue','lightcoral']
explode = (0,0,0.5,0,0.8,0,0,0)
plt.pie(marketshare,
explode = explode,
labels = labels,
colors = colors,
autopct="%.1f%%",
shadow=True,
startangle=45)
plt.axis("equal")
plt.title("Web Browser Marketshare - 2021")
plt.show()