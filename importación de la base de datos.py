#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
from urllib.request import urlopen 
html = urlopen("http://52.91.80.124:8080/quotes").read()
df = pd.read_json(html)


# # importamos os datos provenientes de la api 

# In[3]:


df


# # instalamos los servicios que requeriremos para poder ejecutar la instancia 

# In[4]:


pip install sqlalchemy pymysql


# # Importamos las librerias que usaremos para la extraccion de la base de datos.

# In[6]:


import psycopg2
host = 'ubuntu2021.cxhh9fgxhh6a.us-east-1.rds.amazonaws.com'
port = 5432
dbname = 'ubuntu2021'
username = 'ubuntu2021'
pwd = 'ubuntu2021'

conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, username, pwd))
sql = "select * from quotes;"
dat = pd.read_sql_query(sql, conn)
conn = None


# # Importamos los datos 

# In[7]:


dat


# In[ ]:




