#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import random
x=random.pareto(a=2,size=(2,3))
print(x)


# In[2]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()


# In[3]:


import numpy as np
from numpy import random
x=random.zipf(a=2,size=(2,3))
print(x)


# In[4]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=random.zipf(a=2,size=1000)
sns.distplot(x[x<10],kde=False)
plt.show()


# In[ ]:




