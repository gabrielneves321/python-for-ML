#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
ages = np.array([34,12,37,5,13])
sorted_ages = np.sort(ages)
print("The sorted ages are:", sorted_ages)
print("The ages are:", ages)


# In[3]:


import numpy as np
ages = np.array([34,12,37,5,13])
print("The  ages are:", ages)
ages.sort()
print("The sorted ages are:", ages)


# In[4]:


import numpy as np
ages = np.array([34,12,37,5,13])
print("The index of the sorted ages are:", ages.argsort())


# In[5]:


import numpy as np
ages = np.array([34,12,37,5,13])
print("The  ages are:", ages[ages.argsort()])


# In[6]:


import numpy as np
persons = np.array(['Jhony','Mary','Peter','Will','Joe'])
ages = np.array([34,12,37,5,13])
heights = np.array([1.76,1.2,1.68,0.5,1.25])
sort_indices = np.argsort(ages)
print("The sorted names with respect to ages are:", persons[sort_indices])
print("The sorted ages are:", ages[sort_indices])
print("The sorted heights with respect to ages are:", heights[sort_indices])


# In[7]:


import numpy as np
persons = np.array(['Jhony','Mary','Peter','Will','Joe'])
ages = np.array([34,12,37,5,13])
heights = np.array([1.76,1.2,1.68,0.5,1.25])
sort_indices = np.argsort(persons)
print("The sorted names are:", persons[sort_indices])
print("The sorted ages with respect to names are:", ages[sort_indices])
print("The sorted heights with respect to names are:", heights[sort_indices])


# In[8]:


import numpy as np
persons = np.array(['Jhony','Mary','Peter','Will','Joe'])
ages = np.array([34,12,37,5,13])
heights = np.array([1.76,1.2,1.68,0.5,1.25])
reverse_sort_indices=np.argsort(persons)[::-1]
print("The reverse sorted names are:", 
      persons[reverse_sort_indices])
print("The reverse sorted ages with respect to names are:",
      ages[reverse_sort_indices])
print("The reverse sorted heights with respect to names are:", 
      heights[reverse_sort_indices])


# In[ ]:




