#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpy import random
x=random.exponential(scale=2,size=(2,3))
print(x)


# In[3]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000),hist=False)
plt.show()


# In[5]:


import numpy as np
from numpy import random
x=random.chisquare(df=2,size=(2,3))
print(x)


# In[7]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1,size=1000),hist=False)
plt.show()


# In[8]:


import numpy as np
from numpy import random
x=random.rayleigh(scale=2,size=(2,3))
print(x)


# In[10]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000),hist=False)
plt.show()


# In[11]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000),hist=False)
sns.distplot(random.chisquare(df=2,size=(2,3)),hist=False)
plt.show()


# In[ ]:




