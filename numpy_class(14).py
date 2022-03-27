#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


# In[3]:


import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)


# In[4]:


import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)


# In[6]:


import numpy as np 
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7)
print(x)


# In[7]:


import numpy as np 
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7,side='right')
print(x)


# In[9]:


import numpy as np 
arr = np.array([1,3,5,7])
x = np.searchsorted(arr,[2,4,6])
print(x)


# In[10]:


import numpy as np
arr=np.array([41,42,43,44])
x=[True,False,True,False]
newarr=arr[x]
print(newarr)


# In[23]:


import numpy as np
arr=np.array([41,42,43,44])
filter_arr=[]
for element in arr:
    if element>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)
            


# In[24]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
filter_arr=[]
for element in arr:
    if element%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)


# In[25]:


import numpy as np
arr=np.array([41,42,43,44])
filter_arr= arr>42
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)


# In[26]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
filter_arr= arr%2 == 0
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)


# In[ ]:




