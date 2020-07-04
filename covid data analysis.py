#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly
import plotly.express as px
import plotly.grapg_objects as go

import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

import folium


# In[2]:


get_ipython().system('pip install pandas')


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly
import plotly.express as px
import plotly.graph_objects as go

import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

import folium


# In[4]:


pyo.init_notebook_mode(connected = True)
cf.go_offline()


# In[5]:


df = pd.read_excel(r"C:\Users\hp\Desktop\Projects\covid 19 data analysis\Covid country wise cases.xlsx")


# In[6]:


pip install xlrd


# In[7]:


df = pd.read_excel(r"C:\Users\hp\Desktop\Projects\covid 19 data analysis\Covid country wise cases.xlsx")


# In[8]:


df


# In[9]:


total_overall_cases = df['Total Cases'].sum()
print("Total overall cases in the top 10 covid infected countries till now are :", total_overall_cases)


# In[10]:


df.style.background_gradient(cmap = 'Reds')


# In[11]:


Total_active_cases = df.groupby('Country')['Active Cases'].sum().sort_values(ascending = False).to_frame()


# In[12]:


Total_active_cases


# In[13]:


Total_active_cases.style.background_gradient(cmap = 'Reds')


# In[14]:


df.iplot(kind = 'bar', x = 'Country', y = 'Active Cases', xTitle = 'Country', yTitle = 'Active Cases')


# In[15]:


df.iplot(kind = 'bar', x = 'Country', y = 'Total Cases', xTitle = 'Country', yTitle = 'Total Cases')


# In[16]:


px.bar(df,x = 'Country', y = 'Active Cases')


# In[17]:


px.bar(df,x = 'Country', y = 'Serious Cases')


# In[18]:


df.iplot(kind = 'scatter', x = 'Country', y = 'Total Cases',mode = 'markers + lines',title = 'Graph representing Total Cases vs Country', xTitle = 'Country', yTitle = 'Total Cases')


# In[19]:


df.iplot(kind = 'scatter', x = 'Country', y = 'Serious Cases', mode = 'markers + lines',title = 'Graph representing Serious Cases vs Country', xTitle = 'Country', yTitle = 'Serious Cases')


# In[39]:


df.iplot(kind = 'scatter', x = 'Country', y = 'Active Cases', title = 'Graph representing Active Cases vs Country',mode = 'markers + lines', xTitle = 'Country', yTitle = 'Active Cases')


# In[22]:


world_coordinates = pd.read_excel(r"C:\Users\hp\Desktop\Projects\covid 19 data analysis\mapping coordinates of countries.xlsx")


# In[23]:


world_coordinates


# In[24]:


df_full = pd.merge(world_coordinates,df,on = 'Country')


# In[25]:


df_full


# In[26]:


map = folium.Map(location = [10,60], zoom_start = 4, tiles = 'Stamenterrain')

for lat, long, value, name in zip(df_full['Latitude'],df_full['Longitude'],df_full['Total Cases'],df_full['Country']):
    folium.CircleMarker([lat,long], radius = value * 10, popup = ('<strong>State</strong>:'+ str(name).capitalize() + '<br>''<strong> Total Cases </strong>:' + str(value) + '<br'), color = 'red', full_color = 'red', fill_opacity = 0.5).add_to(map)
    


# In[27]:


map = folium.Map(location = [20,70], zoom_start = 4, tiles = 'Stamenterrain')

for lat, long, value, name in zip(df_full['Latitude'],df_full['Longitude'],df_full['Total Cases'],df_full['Country']):
    folium.CircleMarker([lat,long], radius = value * 10, popup = ('<strong>State</strong>:'+ str(name).capitalize() + '<br>''<strong>Total Cases</strong>:' + str(value) + '<br>'), color = 'red', fill_color = 'red', fill_opacity = 0.5).add_to(map)
    


# In[ ]:




