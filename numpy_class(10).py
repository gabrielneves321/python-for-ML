#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr =np.array([1,2,3,4,5])
arr1 = arr.copy()
arr[0] = 42
print(arr)
print(arr1)


# In[4]:


import numpy as np
arr =np.array([1,2,3,4,5])
arr1 = arr.view()
arr[0] = 42
print(arr)
print(arr1)


# In[5]:


import numpy as np
arr =np.array([1,2,3,4,5])
arr1 = arr.view()
arr1[0] = 31
print(arr)
print(arr1)


# In[6]:


import numpy as np
arr =np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)


# In[7]:


import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)


# In[8]:


import numpy as np
arr =np.array([1,2,3,4], ndmin=5)
print(arr)
print("Shape of the array:", arr.shape)


# In[9]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)


# In[10]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)


# In[11]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,])
newarr = arr.reshape(3,3)
print(newarr)


# In[12]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
newarr = arr.reshape(3,3)
print(newarr)


# In[13]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,])
print(arr.reshape(2,4).base)


# In[17]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1)
print(newarr)


# In[18]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,2)
print(newarr)


# In[19]:


import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
newarr = arr.reshape(-1)
print(newarr)


# In[ ]:




