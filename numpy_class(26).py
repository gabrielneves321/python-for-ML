#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
num1=6
num2=18
x=np.lcm(num1,num2)
print(x)


# In[5]:


import numpy as np
arr=np.array([3,6,9])
x=np.lcm.reduce(arr)
print(x)


# In[6]:


import numpy as np
arr=np.arange(1,11)
x=np.lcm.reduce(arr)
print(x)


# In[7]:


import numpy as np
num1=6
num2=9
x=np.gcd(num1,num2)
print(x)


# In[8]:


import numpy as np
arr=np.array([20,8,32,36,16])
x=np.gcd.reduce(arr)
print(x)


# In[ ]:




