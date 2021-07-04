#!/usr/bin/env python
# coding: utf-8

# In[164]:


import numpy as np
import pandas as pd
import re

file1=pd.read_csv("Cost_of_living_index.csv")
file1['City'] = file1['City'].str.upper() 
print(len(file1['City']))
      
pd.set_option('display.max_rows', None)
file2=pd.read_csv("crime_data.csv")
print(len(file2['City']))
      
a=pd.merge(file1, file2, how='left', on='City')
a.to_csv("data_1.csv")
a.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[161]:


file3=pd.read_csv("rent_price_index.csv")
file3["City"]=file3["City"].str.upper()
file3[['City','State','Country']] = file3.City.str.split(",",expand=True,)
file3.sort_values('City')
a.sort_values('City')
print (len(file3['City']))
print(len(a['City']))
c=pd.merge(b,file3,how='left',left_on='City',right_on='City')
c.to_csv("data_2.csv")
c = c[c.id != 'NaN']
c


# In[ ]:


file5=pd.read_csv("covid_clusters.csv")
file5["state"]=file5["state"].str.upper()
d=pd.merge(c,file5,how='left',left_on='State_y',right_on='state')
d.to_csv("data_4.csv")


# In[ ]:


file6=pd.read_csv("population.csv")
file6["NAME"]=file6["NAME"].str.upper()
file6[['City','U/R']] = file6.NAME.str.split(" ",expand=True,)
e=pd.merge(d,file6,how='left',left_on='City',right_on='NAME')
e.to_csv("data_5.csv")

