#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list=[1,2,3,4,5]
arr= np.array(list)
print("The Numpy array is:", arr)
arr1=arr.reshape(1,-1)
print("The Reshape Numpy array is:", arr1)


# In[2]:


import numpy as np
list=[1,2,3,4,5]
arr= np.array(list)
print("The Numpy array is:", arr)
print(arr.shape)
arr1=arr.reshape(1,-1)
print("The Reshape Numpy array is:", arr1)
print(arr1.shape)


# In[8]:


import numpy as np
list = [1,2,3,4,5]
arr = np.array(list)
print("The Numpy array is:", arr)
print(arr.shape)
arr1 = arr.reshape(1,-1)
print("The Reshape Numpy array is:", arr1)
print(arr1.shape)
arr2 = arr1.reshape(1,-1)
print(arr2)


# In[9]:


import numpy as np
list = [1,2,3,4,5]
arr = np.array(list)
print("The Numpy array is:", arr)
print(arr.shape)
arr1 = arr.reshape(1,-1)
print("The Reshape Numpy array is:", arr1)
print(arr1.shape)
arr2 = arr1.reshape(1,1,-1)
print(arr2)


# In[11]:


import numpy as np
list = [1,2,3,4,5]
arr = np.array(list)
print("The Numpy array is:", arr)
print(arr.shape)
arr1 = arr.reshape(1,-1)
print("The Reshape Numpy array is:", arr1)
print(arr1.shape)
arr2 = arr1.reshape(1,1,1,-1)
print(arr2)
print(arr2.shape)


# In[12]:


import numpy as np
list=[1,2,3,4,5]
arr1= np.array([list])
print("The numpy array is:", arr1)
arr=arr1.reshape(-1,)
print("The reshape numpy is:", arr)


# In[14]:


import numpy as np
list=[1,2,3,4,5]
arr1= np.array([list])
print("The numpy array is:", arr1)
arr=arr1.flatten()
print("The reshape numpy array is:", arr)


# In[15]:


import numpy as np
list=[1,2,3,4,5]
arr1= np.array([list])
print("The numpy array is:", arr1)
arr=arr1.ravel()
print("The reshape numpy is:", arr)


# In[16]:


import numpy as np
arr = np.array([1,2,3,4])
print("The data type of arr is:", arr.dtype)


# In[17]:


import numpy as np
arr= np.array(['apple','banana','orange'])
print("The data type of arr is:", arr.dtype)


# In[19]:


import numpy as np
arr=np.array([1,2,3,4], dtype='S')
print("The value of arr is:", arr)
print("The data type of arr is:", arr.dtype)


# In[20]:


import numpy as np
arr=np.array([1,2,3,4], dtype='i4')
print("The value of arr is:", arr)
print("The data type of arr is:", arr.dtype)


# In[21]:


import numpy as np
arr=np.array([1,2,3,4], dtype='i8')
print("The value of arr is:", arr)
print("The data type of arr is:", arr.dtype)


# In[22]:


import numpy as np
arr=np.array(['a','2','3'],  dtype='i')
print("The value of arr is:", arr)


# In[23]:


import numpy as np
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print("The value of newarr is:", newarr)
print("The data type of newarr is:", newarr.dtype)


# In[24]:


import numpy as np
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype(int)
print("The value of newarr is:", newarr)
print("The data type of newarr is:", newarr.dtype)


# In[25]:


import numpy as np
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print("The value of newarr is:", newarr)
print("The data type of newarr is:", newarr.dtype)


# In[26]:


import numpy as np
arr = np.array([1.5,3.7,3.4])
newarr = arr.astype(bool)
print("The value of newarr is:", newarr)
print("The data type of newarr is:", newarr.dtype)


# In[ ]:




