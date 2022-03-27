#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from numpy import random
x=random.binomial(n=10,p=0.5,size=10)
print(x)


# In[7]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True,kde=False)
plt.show()


# In[10]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50,scale=5,size=1000),hist=False,label='normal')
sns.distplot(random.binomial(n=100,p=0.5,size=1000),hist=False,label='binomial')
plt.show()         


# In[12]:


import numpy as np
from numpy import random
x=random.poisson(lam=2,size=10)
print(x)


# In[13]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2,size=1000),kde=False)
plt.show()


# In[14]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50,scale=7,size=1000),hist=False,label='normal')
sns.distplot(random.poisson(lam=50,size=1000),hist=False,label='poisson')
plt.show()


# In[15]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=1000,p=0.01,size=1000),hist=False,label='binomial')
sns.distplot(random.poisson(lam=10,size=1000),hist=False,label='poisson')
plt.show()


# In[ ]:




