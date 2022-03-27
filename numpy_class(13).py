#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
print("The original array is:")
print(arr)
newarr=np.array_split(arr,3)
print("The splitted array is:")
print(newarr)


# In[5]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
print("The original array is:")
print(arr)
newarr=np.array_split(arr,4)
print("The splitted array is:")
print(newarr)


# In[10]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[9]:


import numpy as np
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr = np.array_split(arr, 3)
print(newarr)


# In[12]:


import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.array_split(arr, 3)
print(newarr)


# In[13]:


import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)


# In[14]:


import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.hsplit(arr, 3)
print(newarr)


# In[15]:


import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr = np.vsplit(arr, 3)
print(newarr)


# In[19]:


import numpy as np
arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]])
newarr = np.dsplit(arr, 3)
print(newarr)


# In[ ]:




