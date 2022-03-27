#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)


# In[2]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1
print("The value os array2 is:")
print(array2)


# In[4]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1
print("The value os array2 is:")
print(array2)
array2[0][0]=11
print("The update array2 is:")
print(array2)
print("The update array1 is:")
print(array1)


# In[5]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1
print("The value os array2 is:")
print(array2)
array1.shape = 1,-1
print("The updated value of array1 is:")
print(array1)
print("The updated value of array2 is:")
print(array2)


# In[6]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1.view()
print("The value os array2 is:")
print(array2)


# In[9]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1.view()
print("The value os array2 is:")
print(array2)
array1[0][0] = 11
print("The updated value of array1 is:")
print(array1)
print("The updated value of array2 is:")
print(array2)


# In[10]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1.view()
print("The value os array2 is:")
print(array2)
array1.shape = 1, -1
print("The updated value of array1 is:")
print(array1)
print("The updated value of array2 is:")
print(array2)


# In[11]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
array2 = array1.copy()
print("The value of array1 is:")
print(array1)
print("The value os array2 is:")
print(array2)


# In[12]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1.copy()
print("The value os array2 is:")
print(array2)
array1[0][0] = 11
print("The updated value of array1 is:")
print(array1)
print("The value of array2 is:")
print(array2)


# In[13]:


import numpy as np
list = [[1,2,3], [4,5,6]]
array1 = np.array(list)
print("The value of array1 is:")
print(array1)
array2 = array1.copy()
print("The value os array2 is:")
print(array2)
array1.shape = 1, -1
print("The updated value of array1 is:")
print(array1)
print("The value of array2 is:")
print(array2)


# In[ ]:




