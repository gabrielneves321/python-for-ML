#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a1 = np.arange(10) #creates a range from 0 to 9
print(a1) # [0 1 2 3 4 5 6 7 8 9]
print(a1.shape) # (10,)


# In[3]:


import numpy as np
a2 = np.arange(0,10,3) #creates a range from 0 to 9, step 2
print(a2) #[0 2 4 6 8]
print(a2.shape)


# In[4]:


import numpy as np
a3 = np.zeros(5) #create an array with all 0s
print(a3) #[0, 0, 0, 0, 0]
print(a3.shape) # (5,)


# In[5]:


import numpy as np
a4 = np.zeros((2,3)) # array of rank 2 with all 0s; 2 rows and 3 # colums
print(a4)
print(a4.shape) #(2,3)


# In[8]:


import numpy as np
a5 = np.full((2,3), 8) #array of rank 2 with all 8s
print(a5)
print(a5.shape)


# In[9]:


import numpy as np
a6 = np.eye(4) # 4x4 identity matrix
print(a6)
print(a6.shape)


# In[10]:


import numpy as np
a7 = np.random.random((2,4)) # rank 2 array (2 rows 4 columns) with random values in the half-open interval [0.0,1.0]
print(a7)
print(a7.shape)


# In[11]:


list1 = [1,2,3,4,5] #list in python
print(list1)
r1 = np.array(list1) # rank 1 array
print(r1) 


# In[ ]:




