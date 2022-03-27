#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=[1,2,3,4]
y=[4,5,6,7]
z=[]
for i, j in zip(x,y):
    z.append(i+j)
print(z)


# In[2]:


import numpy as np
x=[1,2,3,4]
y=[4,5,6,7]
z=np.add(x,y)
print(z)


# In[11]:


import numpy as np
def myadd(x,y):
    return x+y
myadd=np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4], [5,6,7,8]))


# In[12]:


import numpy as np
print(type(np.add))


# In[14]:


import numpy as np
print(type(np.concatenate))


# In[15]:


import numpy as np
print(type(np.xyz))


# In[17]:


import numpy as np
if type(np.add)==np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')


# In[19]:


import numpy as np
if type(np.concatenate)==np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')


# In[ ]:




