#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.array([1,2,3,4])
x=np.prod(arr)
print(x)


# In[3]:


import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
x=np.prod([arr1,arr2])
print(x)


# In[4]:


import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
newarr=np.prod([arr1,arr2],axis=1)
print(newarr)


# In[6]:


import numpy as np
arr=np.array([5,6,7,8])
newarr=np.cumprod(arr)
print(newarr)


# In[7]:


import numpy as np
arr=np.array([10,15,25,5])
newarr=np.diff(arr)
print(newarr)


# In[8]:


import numpy as np
arr=np.array([10,15,25,5])
newarr=np.diff(arr,n=2)
print(newarr)


# In[ ]:




