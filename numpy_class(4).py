#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=[1,2,3,4,5]
arr=list[1:3]
print(arr)


# In[2]:


import numpy as np
arr = np.array([[1,2,3,4,5], [4,5,6,7,8], [9,8,7,6,5]])
print("The numpy Array is:")
print(arr)
arr1 =arr[1:3, :3] # row 1 to 3 (not inclusive) and first 3 columns
print("The Sliced Numpy Array is:")
print(arr1)


# In[4]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])


# In[6]:


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])


# In[7]:


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])


# In[8]:


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])


# In[9]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])


# In[10]:


import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[::2])


# In[11]:


import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, 1:4])


# In[12]:


import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0:2, 2])


# In[13]:


import numpy as np
arr =np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0:2, 1:4])


# In[15]:


import numpy as np
arr = np.array([[1,2,3,4,5], [4,5,6,7,8], [9,8,7,6,5]])
print("The numpy array is:")
print(arr)
arr1 = arr[1:, 2:]
print("The sliced Numpy Array is:")
print(arr1)


# In[16]:


import numpy as np
arr = np.array([[1,2,3,4,5], [4,5,6,7,8], [9,8,7,6,5]])
print(arr)
arr1 = arr[1:, 2:]
print("The sliced Numpy Array is:")
print(arr1)
arr1[0,2]=88
print("Update numpy array")
print(arr)


# In[17]:


import numpy as np
arr = np.array([[1,2,3,4,5], [4,5,6,7,8], [9,8,7,6,5]])
print("The numpy array is:")
print(arr)
arr1 = arr[2:, :]
print("The sliced Numpy Array is:")
print(arr1)
print("The shape of sliced numpy array is")
print(arr1.shape)


# In[28]:


import numpy as np
arr = np.array([[1,2,3,4,5], [4,5,6,7,8], [9,8,7,6,5]])
print("The numpy array is:")
print(arr)
arr1 = arr[2, :]
print("The sliced Numpy Array is:")
print(arr1)
print("The shape of sliced numpy array is")
print(arr1.shape)


# In[ ]:




