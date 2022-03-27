#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list=[1,2,3,4,5]
arr=np.array(list)
print(arr)
print(type(arr))


# In[3]:


import numpy as np
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=[11,12,13,14,15]
arr=np.array([list1,list2,list3])
print(arr)
print(type(arr))


# In[4]:


import numpy as np
tuple= (1,2,3,4,5)
arr = np.array(tuple)
print(arr)
print(type(arr))


# In[5]:


import numpy as np
set = {1,2,3,4,5}
arr = np.array(set)
print(arr)
print(type(arr))


# In[6]:


import numpy as np
dic = {"Name":"Gabriel", "Surname": "Neves"}
arr = np.array(dic)
print(arr)
print(type(arr))


# In[8]:


import numpy as np
arr = np.array(10)
print(arr)
print(type(arr))


# In[9]:


import numpy as np
list = [6,7,8,9,10]
arr = np.array(list)
print(arr)
print(type(arr))


# In[11]:


import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# In[12]:


import numpy as np
set1 ={1,2}
set2 ={3,4}
arr = np.array([set1, set2])
print(arr)


# In[13]:


import numpy as np
arr = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(arr)


# In[14]:


import numpy as np
list1=[1,2,3]
list2=[4,5,6]
arr = np.array([[list1,list2]])
print(arr)


# In[15]:


import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,6]]])
print("Dimension of a is:",a.ndim)
print("Dimension of b is", b.ndim)
print("Dimension of c is", c.ndim)
print("Dimension of d is", d.ndim)


# In[17]:


import numpy as np
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print("number of dimensions:",arr.ndim)


# In[18]:


import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)


# In[ ]:




