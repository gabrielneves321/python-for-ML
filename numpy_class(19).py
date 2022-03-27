#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from numpy import random
x=random.uniform(size=(2,3))
print(x)


# In[6]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000),hist=False)
plt.show()


# In[9]:


import numpy as np
from numpy import random
x=random.logistic(loc=1,scale=2,size=(2,3))
print(x)


# In[11]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000),hist=False)
plt.show()


# In[13]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(loc=2,scale=3,size=1000),hist=False)
plt.show()


# In[14]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(scale=2,size=1000),hist=False,label='normal')
sns.distplot(random.logistic(size=1000),hist=False,label='logistic')
plt.show()


# In[17]:


import numpy as np
from numpy import random
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)


# In[19]:


import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6], size=10),hist=False,label='multinomial')
plt.show()


# In[ ]:




