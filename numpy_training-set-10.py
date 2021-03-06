# -*- coding: utf-8 -*-
"""Untitled71.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bY10AoAiyBkxidf-mQkNh16IPBam5Rck
"""

import numpy as np
A = np.random.randn(4,5)
B = np.random.randn(5,4)
Z = np.dot(A,B)
print(Z)

import numpy as np
row1 = [10,12,13]
row2 = [45,32,16]
row3 = [45,32,16]
nums_2d = np.array([row1,row2,row3])
multiply = np.multiply(nums_2d,nums_2d)
print(multiply)

import numpy as np
row1 = [1,2,3]
row2 = [5,2,8]
row3 = [9,1,10]
nums_2d = np.array([row1,row2,row3])
inverse = np.linalg.inv(nums_2d)
print(inverse)

import numpy as np
row1 = [1,2,3]
row2 = [5,2,8]
row3 = [9,1,10]
nums_2d = np.array([row1,row2,row3])
trace = np.trace(nums_2d)
print(trace)

import numpy as np
A = np.array([[6,3],[2,4]])
B = np.array([42,32])

A_inv = np.linalg.inv(A)
print(A_inv)

X = np.dot(A_inv,B)
print(X)

# Commented out IPython magic to ensure Python compatibility.
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
np.random.seed(0)
X,y = datasets.make_moons(100,noise=0.10)
x1 = X[:,0]
x2 = X[:,1]
plt.figure(figsize=(10,7))
plt.scatter(x1,x2,c=y,cmap=plt.cm.coolwarm)

y = y.reshape(y.shape[0],1)

print(X.shape)
print(y.shape)

def define_parameters(weights):
    weight_list = []
    bias_list = []
    for i in range(len(weights) - 1):
        w = np.random.randn(weights[i],weights[i+1])
        b = np.random.randn()
    weight_list.append(w)
    bias_list.append(b)

    return weight_list,bias_list

def sigmoid(x):
    return1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

def predictions(w, b, X):
    zh = np.dot(X,w[0]) + b[0]
    ah = sigmoid(zh)
    zo = np.dot(ah,w[1]) + b[1]
    ao = sigmoid(zo)
    return ao

def find_cost(ao,y):
    m = y.shape[0]
    total_cost = (1/m) * np.sum(np.square(ao - y))
    return total_cost

def find_derivates(w,b,X):
    zh = np.dot(X,w[0]) + b[0]
    ah = sigmoid(zh)
    zo = np.dot(ah, w[1]) + b[1]
    ao = sigmoid(zo)
    # Backpropagation phase 1
    m = y.shape[0]
    dcost_dao = (1/m)*(ao-y)
    dao_dzo = sigmoid_der(zo)
    dzo_dwo = ah.T
    dwo = np.dot(dzo_dwo,dcost_dao*dao_dzo)
    dbo = np.sum(dcost_dao*dao_dzo)
    # Backpropagation phase 2
    # dcost_wh = dcost_dah * dah_dzh * dzh_dwh
    # dcost_dah = dcost_dzo * dzo_dah
    dcost_dzo = dcost_dao*dao_dzo
    dzo_dah = w[1].T
    dcost_dah = np.dot(dcost_dzo,dzo_dah)
    dah_dzh = sigmoid_der(zh)
    dzh_dwh = X.T
    dwh = np.dot(dzh_dwh, dah_dzh * dcost_dah)
    dbh = np.sum(dah_dzh * dcost_dah)
    return dwh, dbh, dwo, dbo

def update_weights(w,b,dwh, dbh, dwo, dbo, lr):
    w[0] = w[0] - lr * dwh
    w[1] = w[1] - lr * dwo
    b[0] = b[0] - lr * dbh
    b[1] = b[1] - lr * dbo
    return w, b

def my_neural_network(X,y,lr,epochs):
    error_list = []
    input_len = X.shape[1]
    output_len = y.shape[1]
    w,b = define_parameters([input_len,4,output_len])
    for i in range(epochs):
        ao = predictions(w,b,X)
        cost = find_cost(ao,y)
        error_list.append(cost)
        dwh,dbh,dwo,dbo = find_derivates(w,b,X)
        w , b = update_weights(w, b, dwh, dbh, dwo, dbo, lr)
        if i % 50 == 0 :
            print(cost)
   return w, b, error_list