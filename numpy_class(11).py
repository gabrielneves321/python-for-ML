#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr =np.array([1,2,3])
for x in arr:
    print(x)


# In[2]:


import numpy as np
arr =np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)


# In[5]:


import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)


# In[6]:


import numpy as np
arr =np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)


# In[7]:


import numpy as np
arr =np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)


# In[8]:


import numpy as np
arr =np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)


# In[9]:


import numpy as np
arr =np.array([1,2,3])
for x in np.nditer(arr,flags=['buffered'], op_dtypes=['S']):
    print(x)


# In[11]:


import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr[:, ::2]):
    print(x)


# In[12]:


import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr[:, ::3]):
    print(x)


# In[13]:


import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr[:, ::1]):
    print(x)


# In[18]:


import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr[1:, ::2]):
    print(x)


# In[19]:


import numpy as np
arr =np.array([1,2,3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)


# In[21]:


import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)


# In[22]:


import numpy as np
arr=np.array([[[1,2,3]]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)


# In[ ]:




