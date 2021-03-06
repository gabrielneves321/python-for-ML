# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DeSZXUpTYhy7b4Dms6SsEku9od48S3mR
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
  return (x ** 3 + y ** 2)
n = 10
x = np.linspace(-3, 3, 8 * n)
y = np.linspace(-3, 3, 6 * n)
X, Y = np.meshgrid(x, y)
Z = f( X, Y )
plt.imshow(Z, interpolation='nearest',
            cmap = 'cool', origin='lower')
plt.axis('off')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (x ** 3 + y ** 2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
plt.contourf(X, Y, f(X, Y), 8,
              alpha = 0.75, cmap='hot')
C = plt.contour(X, Y, f(X, Y), 8,
colors='black')
plt.clabel(C, inline=1, fontsize=10)
plt.axis('off')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib qt
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1,
            cstride=1, cmap='hot')
ax.contourf(X, Y, Z, zdir='z',
            offset=-2, cmap='hot')
ax.set_zlim(-2, 2)
plt.axis('off')
ax.set_zticks(())
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib qt
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
color = np.arctan2(Y, X)
plt.scatter(X, Y, s=75, c=color, alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axis('off')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib qt
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
N = 100
x = np.arange(N) 
y1 = np.random.randn(N)
y2 = np.random.randn(N)
y3 = np.random.randn(N)
y4 = np.random.randn(N)
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.plot(x, y2, ':')
plt.grid()
plt.xlabel('Time')
plt.ylabel('y1 and y2')
plt.axis('tight')
plt.subplot(2, 1, 2)
plt.plot(x, y3)
plt.plot(x, y4, 'r')
plt.grid()
plt.xlabel('Time')
plt.ylabel('y3 and y4')
plt.axis('tight')
plt.show()

f = 1
t = np.arange(0.0, 4.0, 0.01)
s1 = np.sin(2 *np.pi * f * t)
s2 = np.exp(-t)
s3 = s1 * s2
f = plt.figure()
plt.subplots_adjust(hspace=0.001)
ax1 = plt.subplot( 311 )
ax1.plot(t, s1)
plt.yticks(np.arange(-0.9, 1.0, 0.4))
plt.ylim(-1, 1)
ax2 = plt.subplot(312, sharex=ax1)
ax2.plot(t, s2)
plt.yticks(np.arange(0.1, 1.0, 0.2))
plt.ylim(0, 1)
ax3 = plt.subplot(313, sharex = ax1)
ax3.plot(t, s3)
plt.yticks(np.arange(-0.9, 1.0, 0.4))
plt.ylim(-1, 1)
xticklabels = ax1.get_xticklabels() + ax2.get_xticklabels()
plt.setp(xticklabels, visible=False)
plt.show()

N = 1000
x = np.linspace(0, 1, N)
y = np.sin(4 * np.pi * x) + np.exp(-5 * x)
plt.fill(x, y, 'g', alpha = 0.8)
plt.grid(True)
plt.show()

N = 100
x = np.linspace(-np.pi, np.pi, N)
y1 = 0.5 * np.sin(3*x)
y2 = 1.25 * np.sin(2*x)
y3 = 2 * np.sin(4*x)
plt.plot(x, y1, x, y2, x, y3)
plt.show()

plt.step(x, y1)
plt.step(x, y2)
plt.step(x, y3)
plt.show()

x, y = np.random.normal(size=(2, 10000))
plt.hexbin(x, y, gridsize=20, cmap='cool')
plt.colorbar()
plt.show()

y = np.random.randn(1000)
plt.xkcd()
plt.hist(y)
plt.show()

y = np.random.randn(1000)
plt.xkcd()
plt.hist(y, bins = 30, range=[-3.5, 3.5],
        facecolor='r',alpha=0.6,edgecolor='k')
plt.grid()
plt.show()

data = np.random.randn(1000, 1000)
plt.xkcd()
plt.hist2d(data[0], data[1])
plt.show()