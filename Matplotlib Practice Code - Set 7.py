# -*- coding: utf-8 -*-
"""Untitled96.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NilryL3W7-3FxqLjFgpIVmqGMuJkDHv9
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3, 3, 0.005)
y = np.arange(-3, 3, 0.005)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2)
out = plt.contour(X, Y, Z)
plt.clabel(out, inline=True,fontsize=10)
plt.show()

x = np.arange(-3, 3, 0.005)
y = np.arange(-3, 3, 0.005)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2)
out = plt.contour(X, Y, Z)
plt.clabel(out, inline=True,fontsize=10)
plt.colorbar(out)
plt.show()

x = np.arange(-3, 3, 0.005)
y = np.arange(-3, 3, 0.005)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2)
out = plt.contour(X, Y, Z, colors='g')
plt.clabel(out, inline=True, fontsize=10)
plt.show()

x = np.arange(-3, 3, 0.005)
y = np.arange(-3, 3, 0.005)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2)
plt.contourf(X, Y, Z, hatches=['-', '/', '\\', '//'],
cmap='cool', alpha=0.75)
plt.show()

Y, X = np.mgrid[-5:5:200j, -5:5:300j]
U = X**2 + Y**2
V = X + Y
plt.streamplot(X, Y, U, V)
plt.show()

Y, X = np.mgrid[-5:5:200j, -5:5:300j]
U = X**2 + Y**2
V = X + Y
plt.streamplot(X, Y, U, V, density=[0.5, 0.75])
plt.show()

Y, X = np.mgrid[-5:5:200j, -5:5:300j]
U = X**2 + Y**2
V = X + Y
plt.streamplot(X, Y, U, V, color=V,
linewidth=1, cmap='cool')
plt.show()

Y, X = np.mgrid[-5:5:200j, -5:5:300j]
U = X**2 + Y**2
V = X + Y
plt.streamplot(X, Y, U, V,density=0.6,
color='k',linewidth=X)
plt.show()

X = np.arange(-5, 5, 0.5)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
plt.quiver(X, Y, U, V)
plt.show()

