# -*- coding: utf-8 -*-
"""Untitled54.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KsZZ8_oIlnH2GRp-BLL0-sxBzEw24Rog

SCIPY SPECIAL FUNCTIONS:
scipy.special.jn()
scipy.special.ellipj()
scipy.special.gamma()
scipy.special.gammaln()
scipy.special.erf()
"""

from scipy import linalg
import numpy as np

#will take the given square matrix as a parameter and return the determinant of that.
arr = np.array([[1,2],[3,4]])

print(linalg.det(arr))


#1*4-2*3 = 4-6 = -2

#works only with 2D arrays
linalg.det(np.ones((1,2)))

#Compute the (multiplicative) inverse of a matrix.
linalg.inv(arr)

##works only with 2D arrays
linalg.inv(np.ones((1,2)))

#Factorizes the matrix a into two unitary matrices U and Vh, and a 1-D array s of singular values
linalg.svd(arr)

import scipy
scipy.interpolate