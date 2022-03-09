#!/usr/bin/env python
# coding: utf-8

# # Binary Predictors in a Logistic Regression

# Using the same code as in the previous exercise, find the odds of 'duration'. 
# 
# What do they tell you?

# ## Import the relevant libraries

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Apply a fix to the statsmodels library
from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)


# ## Load the data

# Load the ‘Bank_data.csv’ dataset.

# In[2]:


raw_data = pd.read_csv("C:/Users/Praveen B Ronad/Downloads/Bank_data.csv")
raw_data


# In[5]:


data = raw_data.copy()
data['y'] = data['y'].map({'yes': 1, 'no': 0})
data


# In[9]:


data.describe()


# ### Declare the dependent and independent variables

# Use 'duration' as the independet variable.

# In[10]:


y = data['y']
x1 = data['duration']


# ### Simple Logistic Regression

# Run the regression.

# In[11]:


x = sm.add_constant(x1)
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()
results_log.summary()


# In[ ]:





# ### Find the odds of duration

# In[12]:


np.exp(0.0051)


# In[16]:



results_log.predict()


# In[ ]:




