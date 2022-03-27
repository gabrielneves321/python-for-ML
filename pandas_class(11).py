# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Eh5a5h0DLY9DlJtauBQeyjlxnU42P_q
"""

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)

import numpy as np
import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
schools =np.array(["Cambridge","Oxford","Oxford","Cambridge","Oxford"])
df["school"]=schools
print(df)

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df.drop(['China','Japan']))

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df[df.name !='Nad']) #drop row based on column value

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df.drop(df.index[1]))

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df.drop(df.index[[1,2]]))

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df.drop(df.index[-2]))

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df.drop('reports',axis=1))

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df.drop(df.columns[1],axis=1))

import pandas as pd
data={'name':['Janet','Nad','Timothy','June','Amy'],'year':[2012,2012,2013,2014,
2014],'reports':[6,13,14,1,7]}
df=pd.DataFrame(data,index=['Singapore','China','Japan','Sweden','Norway'])
print(df)
print(df.drop(df.columns[[1,2]],axis=1))