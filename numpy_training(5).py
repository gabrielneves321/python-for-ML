# -*- coding: utf-8 -*-
"""Untitled52.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pTV1SnD6_ZbtUPFXFCAER7hmLXcasycU
"""

#creating an array with evenly distributed random numbers using the 'random.rand()' command

import numpy as np

uniform_random = np.random.rand(4,5)
print(uniform_random)

#using 'random.randn()' command to create an array with normal distribution
normal_random = np.random.randn(4,5)
print(normal_random)

#checking the number of dimensions with 'ndim'
#checking the number of columns with 'shape'
my_arr = np.array([10,12,14,16,20,25])
print(my_arr)
print('\nDimensions =',my_arr.ndim)
print('\nShape =',my_arr.shape)

#creating a random sequence by passing the number of trials, probability and size
import numpy as np
binomial_random = np.random.binomial(n=100,p=0.5,size=1000)

print(binomial_random)