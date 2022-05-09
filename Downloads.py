#!/usr/bin/env python
# coding: utf-8

# In[13]:


pip install prettytable


# In[14]:


import numpy as np
import requests
import pandas as pd
from prettytable import PrettyTable
import json
import csv


# In[7]:


#Create a table object Pretty table
tableobj = PrettyTable()
KeyVal = '12608f89-09da-41c1-8353-bc854d8c5f85'


# In[8]:


api_endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
api_endpoint += KeyVal
api_endpoint


# In[19]:


json_data = requests.get(api_endpoint).json()


# In[21]:


cryptodata = json_data ['data']


# In[31]:


for currency in cryptodata:
    curr_name = currency['name']
    curr_price = currency['quote']['USD']['price']
    curr_change_1h = currency['quote']['USD']['percent_change_1h']
    curr_change_24h = currency['quote']['USD']['percent_change_24h']
    curr_change_7d = currency['quote']['USD']['percent_change_7d']
    tableobj.add_row([curr_name, curr_price, curr_change_1h, curr_change_24h, curr_change_7d])


# In[33]:


tableobj.field_names = ['Currency name', 'Currency Price', 'Currency 1h Change', 'Currency 24h Change', 'Currency 7d Change']


# In[34]:


print(tableobj)


# In[35]:


table_txt=tableobj.get_string()
with open ('output.txt', 'w') as file:
    file.write(table_txt)


# In[25]:


requests.get(api_endpoint).json()


# In[37]:


table_csv=tableobj.get_string()
with open ('output.txt', 'w') as file:
    file.write(table_csv)


# In[ ]:




