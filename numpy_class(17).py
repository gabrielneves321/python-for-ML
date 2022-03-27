#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from numpy import random
x=random.normal(size=(2,3))
print(x)


# In[6]:


import numpy as np
from numpy import random
x=random.normal(loc=1,scale=2,size=(2,3))
print(x)


# In[13]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000),hist=False)
plt.show()


# In[ ]:




