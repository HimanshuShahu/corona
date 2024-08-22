#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[52]:


from datetime import datetime
import requests


# In[53]:


data=pd.read_csv(r"C:\Users\himan\OneDrive\Desktop\covid_19_india.csv")


# In[54]:


data.head()


# In[55]:


data=data.rename(columns={'State/UnionTerritory':'States', 'Cured':'Recovery'})


# In[56]:


data.head()


# In[57]:


data=data.drop(['Sno', 'Time','ConfirmedIndianNational','ConfirmedForeignNational'], axis=1)


# In[58]:


data.head()


# # Active Case

# In[59]:


data['Active']=data['Confirmed']-data['Deaths']-data['Recovery']


# In[60]:


data.head()


# In[61]:


data=data.sort_values(['Date', 'States']).reset_index(drop=True)
data['Date']=pd.to_datetime(data['Date'])


# In[62]:


data


# In[63]:


india_cases=data[data['Date']==data['Date'].max()].copy().fillna(0)
india_cases.index=india_cases['States']
india_cases=india_cases.drop(['States', 'Date'], axis=1)


# In[64]:


df=pd.DataFrame(pd.to_numeric(india_cases.sum()), dtype=np.float64).transpose()
df.style.background_gradient(cmap='winter_r', axis=1)


# In[65]:


india_cases.sort_values('Active', ascending=False).style\
.background_gradient(cmap='YlGn_r', subset=['Confirmed'])\
.background_gradient(cmap='BrBG_r', subset=['Deaths'])\
.background_gradient(cmap='BuPu', subset=['Recovery'])\
.background_gradient(cmap='YlOrBr', subset=['Active'])


# In[66]:


def horizontal_bar_chart(df,x,y,title,x_label,y_label,color):
    fig=px.bar(df, x=x,y=y, orientation='h', title=title,
           labels={x.name:x_label,
                  y.name:y_label}, color_discrete_sequence=[color])
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig.show()


# In[67]:


cnf, dth, rec, act='#393e46','#33ccff', '#ff99cc', '#fe9801'


# In[68]:


import plotly.express as px


# In[69]:


import plotly.graph_objs as go


# In[70]:


import plotly.figure_factory as ff


# In[71]:


from plotly.subplots import make_subplots


# In[72]:


from plotly.offline import init_notebook_mode, iplot


# In[73]:


top_10_confirmed_Cases = india_cases.sort_values('Confirmed', ascending=False)[:10]
horizontal_bar_chart(top_10_confirmed_Cases,top_10_confirmed_Cases.Confirmed,top_10_confirmed_Cases.index,
                     'Top 10 States with most confirmed cases', 'Number of confirmed cases (in Thousands)','State Name', cnf)
    

