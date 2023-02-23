#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('iris')
df.head()


# In[32]:


df.drop(labels = 'species', axis = 1, inplace=True)
df.head()


# In[37]:


df['sepal_sum'] = df['sepal_length'] + df['sepal_width']
df.head()


# In[46]:


df['petal_sum'] = df['petal_length'] + df['petal_width']
df.head()


# In[73]:


mean = [np.mean(df['sepal_length']),
        np.mean(df['sepal_width']),
        np.mean(df['sepal_sum']),
        np.mean(df['petal_length']),
        np.mean(df['petal_width']),
        np.mean(df['petal_sum'])]

std = [np.std(df['sepal_length']),
        np.std(df['sepal_width']),
        np.std(df['sepal_sum']),
        np.std(df['petal_length']),
        np.std(df['petal_width']),
        np.std(df['petal_sum'])]

min = [np.min(df['sepal_length']),
        np.min(df['sepal_width']),
        np.min(df['sepal_sum']),
        np.min(df['petal_length']),
        np.min(df['petal_width']),
        np.min(df['petal_sum'])]

max = [np.max(df['sepal_length']),
        np.max(df['sepal_width']),
        np.max(df['sepal_sum']),
        np.max(df['petal_length']),
        np.max(df['petal_width']),
        np.max(df['petal_sum'])]

summary_dict = {'mean' :mean,'std':std,'min':min,'max':max}

summary_df = pd.DataFrame(data = summary_dict)

summary_df

summary_df.rename(index={0:'sepal_length',
                 1:'sepal_width',
                 2:'petal_length',
                 3:'petal_width',
                 4:'sepal_sum',
                 5:'petal_sum'})


# In[ ]:




