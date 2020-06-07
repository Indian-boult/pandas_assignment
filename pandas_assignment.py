#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

print(df.head())

## Ans 1
df.iloc[1,1] = 10055.0
df.iloc[3,1] = 10075.0
df = df.astype({"FlightNumber": int})
print(type(df.iloc[0,1]), end = "\n\n\n\n")

## Ans2
temp_df = df.copy()
from_to = temp_df.From_To.tolist()
temp_df = temp_df.drop(['From_To'], axis = 1)
from_to = [x.split("_") for x in from_to]
From = []
To = []
for i in range(len(from_to)):
    From.append(from_to[i][0])
    To.append(from_to[i][1])

temp_df['From'] = From
temp_df['To'] = To
print(temp_df.head(), end = "\n\n\n\n")

##Ans3
temp_df['From'] = temp_df.From.str.capitalize()
temp_df['To'] = temp_df.To.str.capitalize()
print(temp_df.head(), end = "\n\n\n\n")

## Ans4
df = df.drop(['From_To'], axis = 1)
df["From"] = temp_df["From"]
df["To"] = temp_df["To"]
print(df.head(), end = "\n\n\n\n")


## Ans5
df = df.join(df.RecentDelays.apply(pd.Series).add_prefix('delay_'))
df = df.drop(['RecentDelays'], axis = 1)
print(df.head())


# In[26]:


df = df.join(df.RecentDelays.apply(pd.Series).add_prefix('delay_'))
df = df.drop(['RecentDelays'], axis = 1)
print(df.head())


# In[17]:


temp_df.From.str.capitalize()


# In[10]:





# In[ ]:




