#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.matrix([[1,2],[4,5]])
b = np.matrix([[7,8],[2,3]])
print("The matrix a is:")
print(a)
print("The matrix b is:")
print(b)


# In[2]:


import numpy as np
a = np.matrix([[1,2],[4,5]])
b = np.matrix([[7,8],[2,3]])
c = np.matrix(a)
d = np.matrix(b)
print("The matrix c is:")
print(c)
print("The matrix d is:")
print(d)


# In[3]:


import numpy as np
x1 = np.array([[1,2],[4,5]])
y1 = np.array([[7,8],[2,3]])
print("The product of x1 and y1 is:")
print(x1 * y1)
x2 = np.matrix([[1,2],[4,5]])
y2 = np.matrix([[7,8],[2,3]])
print("The product of x1 and y1 is:")
print(x2 * y2)


# In[4]:


import numpy as np
A = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("The value of array A is:")
print(A)
print("The cumulative sum of all the elements in the array is:")
print(A.cumsum())


# In[6]:


import numpy as np
A = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("The value of array A is:")
print(A)
print("The cumulative sum of all the elements in each column of the array is:")
print(A.cumsum(axis=0))


# In[7]:


import numpy as np
A = np.array([(1,2,3),(4,5,6),(7,8,9)])
print("The value of array A is:")
print(A)
print("The cumulative sum of all the elements in each row of the array is:")
print(A.cumsum(axis=1))


# In[ ]:




