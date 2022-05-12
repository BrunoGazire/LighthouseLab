#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

#Opening the two .CSV files 
df = pd.read_csv("HDI.csv")
df2 = pd.read_csv("world_gdp_data.csv")


df.shape

df.columns

df = df.drop("Coverage", axis = 1).dropna().reset_index(drop = True).drop_duplicates()

df.shape

df.describe()

df2 = df2[["country", "country_comparison_infant_mortality_rate","unemployment_rate", "gdp_per_capita", "country_comparison_population"]]

df2.columns

df2.shape

df2 = df2.dropna().reset_index(drop = True).drop_duplicates()
df2.head(10)


df = df.rename(str.lower, axis = "columns")

output = df.merge(df2, how = "inner", on = "country")

output.drop_duplicates()

output.to_csv("C:/Users/Bruno/OneDrive/Área de Trabalho/Final Project/output.csv")





