# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XNQbnvM9-va8Sb-HSHRoYZlLgNAEVn7H
"""

import math
sq_root = lambda x: math.sqrt(x) if x>0 else x
sq=lambda x: x**2

import pandas as pd
import numpy as np
import math
sq_root=lambda x: math.sqrt(x) if x>0 else x
sq=lambda x: x**2
df=pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df)
print(df.B.apply(sq_root))
print(df.B.apply(sq))

import pandas as pd
import numpy as np
import math
sq_root = lambda x: math.sqrt(x) if x>0 else x
sq=lambda x: x**2
df=pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df)
print(df.apply(sq_root))

import pandas as pd
import numpy as np
import math
sq_root = lambda x: math.sqrt(x) if x>0 else x
sq=lambda x: x**2
df=pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df)
print(df.apply(sq))

import pandas as pd
import numpy as np
import math
sq_root = lambda x: math.sqrt(x) if x>0 else x
sq=lambda x: x**2
df=pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df)
for column in df:
  df[column]=df[column].apply(sq_root)
print(df)

import pandas as pd
import numpy as np
import math
sq_root=lambda x: math.sqrt(x) if x>0 else x
sq = lambda x: x**2
df=pd.DataFrame(np.random.randn(10,4),columns=list('ABCD'))
print(df)
print(df.apply(np.sum, axis=0))
print(df.apply(np.sum, axis=1))

