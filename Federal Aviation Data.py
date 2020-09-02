#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv(r"faa_ai_prelim.csv")


# In[2]:


data = pd.DataFrame(data)


# In[3]:


data2 = data.copy()


# In[4]:


data.head()


# In[5]:


data.info()


# In[11]:


data['ACFT_MAKE_NAME'].value_counts().head()


# In[10]:


data['LOC_STATE_NAME'].value_counts().head()


# In[14]:


data['FATAL_FLAG'] = data['FATAL_FLAG'].fillna(value = "NO")


# In[16]:


data['FATAL_FLAG'].value_counts()


# In[19]:


data['ACFT_MODEL_NAME'].isna().sum()


# In[24]:


data = data[data['ACFT_MODEL_NAME'].notna()]


# In[28]:


data.shape


# In[31]:


data[data['FATAL_FLAG'] == 'Yes']

