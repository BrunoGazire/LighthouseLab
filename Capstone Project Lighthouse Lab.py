#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

#Opening the two .CSV files 
df = pd.read_csv("HDI.csv")
df2 = pd.read_csv("world_gdp_data.csv")






# In[2]:


df.shape


# In[3]:


df.columns


# In[4]:


df = df.drop("Coverage", axis = 1).dropna().reset_index(drop = True).drop_duplicates()


# In[5]:


df.shape


# In[6]:


df.describe


# In[7]:


df2.shape


# In[8]:


df2.columns


# In[9]:


df2 = df2[["country", "country_comparison_infant_mortality_rate","unemployment_rate", "gdp_per_capita", "country_comparison_population"]]


# In[10]:


df2.columns


# In[11]:


df2.shape


# In[12]:


df2 = df2.dropna().reset_index(drop = True).drop_duplicates()
df2.head(10)


# In[13]:


df2.shape


# In[14]:


df2.describe


# In[19]:


df = df.rename(str.lower, axis = "columns")

df


# In[20]:


output = df.merge(df2, how = "inner", on = "country")


# In[21]:


output.shape


# In[22]:


output.drop_duplicates()


# In[23]:


output.to_csv("C:/Users/Bruno/OneDrive/Área de Trabalho/Final Project/output.csv")


# In[ ]:




