#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from numpy import random
x = random.choice([3,5,7,9],p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)


# In[8]:


import numpy as np
from numpy import random
x = random.choice([3,5,7,9],p=[0.1, 0.3, 0.6, 0.0], size=(3,5))
print(x)


# In[10]:


import numpy as np
from numpy import random
arr=np.array([1,2,3,4,5])
print(arr)
random.shuffle(arr)
print(arr)


# In[13]:


import numpy as np
from numpy import random
arr=np.array([1,2,3,4,5])
print(random.permutation(arr))
print(arr)


# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5])
plt.show()


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5],hist=False)
plt.show()


# In[ ]:




