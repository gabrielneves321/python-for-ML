#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2))
print("The concatenated array is:", arr)


# In[2]:


import numpy as np
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
arr = np.concatenate((arr1, arr2), axis=1)
print("The concatenated array along rows is:", arr)


# In[3]:


import numpy as np
arr1 = np.array([[1,2], [3,4]])
print(arr1)
arr2 = np.array([[5,6], [7,8]])
print(arr2)
arr = np.concatenate((arr1, arr2), axis=1)
print("The concatenated array along rows is:", arr)


# In[4]:


import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1, arr2), axis=1)
print("The stacked array is:")
print(arr)


# In[7]:


import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1, arr2), axis=0)
print("The stacked array is:")
print(arr)


# In[9]:


import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.hstack((arr1, arr2))
print("The stacked array along rows is:")
print(arr)


# In[11]:


import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.vstack((arr1, arr2))
print("The stacked array along columns is:")
print(arr)


# In[12]:


import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.dstack((arr1, arr2))
print("The stacked array along height is:")
print(arr)


# In[ ]:




