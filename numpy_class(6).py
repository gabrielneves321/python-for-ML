#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print("Adition of A and B is:")
print(A+B)


# In[2]:


import numpy as np
X = np.array([2,3])
Y = np.array([4,2])
print("Adition of X and Y is:")
print(X+Y)


# In[3]:


import numpy as np
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print("Addition of A and B is:")
print(np.add(A, B))


# In[4]:


import numpy as np
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print("Subtraction of A and B is:")
print(A - B)


# In[5]:


import numpy as np
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print("Multiplication of A and B is:")
print(A * B)


# In[6]:


import numpy as np
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print("Division of A and B is:")
print(A/B)


# In[7]:


import numpy as np
names = np.array(['Nirmal', 'Priyanka', 'Resham'])
heights = np.array([1.5,1.78,1.6])
weights = np.array([65,46,59])
bmi = weights/heights **2
print("The body mass index (BMI) of Nirmal, Priyanka and Resham is:",bmi)
print("Overweight :" , names[bmi>25])
print("Underweight :", names[bmi<18.5])
print("Healthy: ", names[(bmi>=18.5) & (bmi<=25)])


# In[8]:


import numpy as np
x = np.array([2,3])
y = np.array([4,2])
print("The dot product of x and y is:", np.dot(x,y))


# In[9]:


import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7,8],[9,10], [11,12]])
print("The dot product of x and y is:")
print(np.dot(x,y))


# In[ ]:




