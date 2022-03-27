#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr = np.array([1,2,3,4])
print(arr[0])
print(arr[1])


# In[3]:


import numpy as np
arr = np.array([1,2,3,4])
print(arr[2] + arr[3])


# In[6]:


import numpy as np
arr = np.array([[1,2,3,4]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr[0,0])
print(arr[0,3])


# In[7]:


import numpy as np
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
arr = np.array([list1, list2])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr[0, 0])
print(arr[0,1])
print(arr[1,0])


# In[9]:


import numpy as np
list1 = [1,2,3,4,5]
arr = np.array(list1)
print(arr[[1,3]])


# In[10]:


import numpy as np
arr = np.array([[[1,2,3]]])
print(arr[0, 0, 2])


# In[11]:


import numpy as np
arr = np.array([[[1,2,3],[4,5,6]]])
print(arr)
print(arr[0,1,0])


# In[13]:


import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [10,11,12]]])
print(arr)
print(arr[1, 1, 2])


# In[14]:


import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[-1])


# In[16]:


import numpy as np
arr = np.array([[1,2,3,4,5]])
print(arr[0,-2])


# In[19]:


import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(arr[1,-1])


# In[20]:


import numpy as np
list = [6,7,8,9,10]
arr = np.array(list)
print(arr)
print(arr>7)


# In[25]:


import numpy as np
list = [6,7,8,9,10]
arr = np.array(list1)
print(arr)
print(arr>7)
print(arr[arr>7])


# In[26]:


import numpy as np
nums = np.arange(20)
print(nums)
odd_num = nums[nums % 2 == 1]
print(odd_num)


# In[ ]:




