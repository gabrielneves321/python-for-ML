# -*- coding: utf-8 -*-
"""Untitled50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XTPmDQHxACYZRWAb7IHLjqE5dLTz_Eaw

importing the numpy library
"""

import numpy as np

"""creating a 10x10 array with zeros and one elements with the 'np.eye' command"""

a = np.eye(10)
print(a)

"""creating a 3x3 array"""

b = np.array([(2,5,7),(5,3,9),(4,6,5)])
print(b)

"""showing largest element of array with 'mean' command"""

b.max()

"""showing smallest element of array with 'min' command"""

b.min()

"""
summing all array elements with 'sum' command"""

b.sum()

"""showing average of all array values ​​with 'mean' command"""

b.mean()

"""calculating standard deviation of array elements with 'std' command"""

b.std()