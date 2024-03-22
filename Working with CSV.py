#!/usr/bin/env python
# coding: utf-8

# 1. IMPORT PANDAS

# In[1]:


import pandas as pd


# 2. Opening a local csv file

# In[2]:


df = pd.read_csv('aug_train.csv')


# In[3]:


df


# 3. Opening a csv filr from an URL

# In[5]:


import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv: 66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

pd.read_csv(data)


# 4. Sep Parameter

# In[6]:


pd.read_csv('movie_titles_metadata.tsv')


# In[7]:


pd.read_csv('movie_titles_metadata.tsv',sep='\t')


# In[8]:


pd.read_csv('movie_titles_metadata.tsv',sep='\t',names=['sno','name','release_year','rating','votes','genres'])


# 5. Index_col parameter

# In[9]:


pd.read_csv('aug_train.csv',index_col='enrollee_id')


# 6.Header Parameter

# In[10]:


pd.read_csv('test.csv',header=1)


# use_cols parameter

# In[12]:


pd.read_csv('aug_train.csv', usecols=['enrollee_id','gender','education_level'])


# Squeeze Parameters

# In[15]:


pd.read_csv('aug_train.csv',usecols = ['gender'],squeeze=True)


# 9.Skip rows/n rows Parameter

# In[18]:


pd.read_csv('aug_train.csv', skiprows=[0,1])


# In[19]:


pd.read_csv('aug_train.csv', nrows=100)


# 10. Encoding Parameter

# In[20]:


pd.read_csv('zomato.csv')


# In[21]:


pd.read_csv('zomato.csv',encoding = 'latin-1')


# 11. Skip bad lines (didn't find dataset)

# In[24]:


pd.read_csv('BX-Books.csv', sep=';' encoding= "latin-1",error_bad_lines=False)


# 12. dtypes parameter

# In[25]:


pd.read_csv('aug_train.csv')


# In[26]:


pd.read_csv('aug_train.csv',dtype={'target':int})


# In[27]:


pd.read_csv('aug_train.csv',dtype={'target':int}).info()


# 13. Handling Dates

# In[28]:


pd.read_csv('IPL Matches 2008-2020.csv')


# In[30]:


pd.read_csv('IPL Matches 2008-2020.csv').info()


# In[32]:


pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date']).info()


# 14. Convertors

# In[33]:


pd.read_csv('IPL Matches 2008-2020.csv')


# In[34]:


def rename(name):
    if name == 'Royal Challengers Bangalore':
         return 'RCB'
    else:
        return name


# In[35]:


rename('Royal Challengers Bangalore')


# In[36]:


pd.read_csv('IPL Matches 2008-2020.csv',converters = {'team1':rename})


# na_values parameter

# In[37]:


pd.read_csv('aug_train.csv')


# In[38]:


pd.read_csv('aug_train.csv',na_values=['Male'])


# Loading a huge dataset in chunks

# In[41]:


dfs=pd.read_csv('aug_train.csv',chunksize=5000)


# In[42]:


dfs


# In[44]:


for chunks in dfs:
    print(chunks.shape)


# In[ ]:




