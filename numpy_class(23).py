#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr1=np.array([10,20,30,40,50,60])
arr2=np.array([3,5,6,8,2,33])
newarr=np.power(arr1,arr2)
print(newarr)


# In[2]:


import numpy as np
arr1=np.array([10,20,30,4,5,6])
arr2=np.array([3,5,6,8,2,33])
newarr=np.power(arr1,arr2)
print(newarr)


# In[5]:


import numpy as np
arr1=np.array([10,20,30,40,50,60])
arr2=np.array([3,7,9,8,2,33])
newarr=np.mod(arr1,arr2)
print(newarr)


# In[6]:


import numpy as np
arr1=np.array([10,20,30,40,50,60])
arr2=np.array([3,7,9,8,2,33])
newarr=np.remainder(arr1,arr2)
print(newarr)


# In[7]:


import numpy as np
arr1=np.array([10,20,30,40,50,60])
arr2=np.array([3,7,9,8,2,33])
newarr=np.divmod(arr1,arr2)
print(newarr)


# In[8]:


import numpy as np
arr=np.array([-1,-2,1,2,3,-4])
newarr=np.absolute(arr)
print(newarr)


# In[9]:


import numpy as np
arr=np.trunc([-3.1666,3.6667])
print(arr)


# In[10]:


import numpy as np
arr=np.fix([-3.1666,3.6667])
print(arr)


# In[13]:


import numpy as np
arr=np.around(3.1666,2)
print(arr)


# In[14]:


import numpy as np
arr=np.floor([-3.1666,3.6667])
print(arr)


# In[15]:


import numpy as np
arr=np.ceil([-3.1666,3.6667])
print(arr)


# In[ ]:




