#!/usr/bin/env python
# coding: utf-8

# # Multiple Linear Regression with sklearn - Exercise Solution

# You are given a real estate dataset. 
# 
# Real estate is one of those examples that every regression course goes through as it is extremely easy to understand and there is a (almost always) certain causal relationship to be found.
# 
# The data is located in the file: 'real_estate_price_size_year.csv'. 
# 
# You are expected to create a multiple linear regression (similar to the one in the lecture), using the new data. 
# 
# Apart from that, please:
# -  Display the intercept and coefficient(s)
# -  Find the R-squared and Adjusted R-squared
# -  Compare the R-squared and the Adjusted R-squared
# -  Compare the R-squared of this regression and the simple linear regression where only 'size' was used
# -  Using the model make a prediction about an apartment with size 750 sq.ft. from 2009
# -  Find the univariate (or multivariate if you wish - see the article) p-values of the two variables. What can you say about them?
# -  Create a summary table with your findings
# 
# In this exercise, the dependent variable is 'price', while the independent variables are 'size' and 'year'.
# 
# Good luck!

# ## Import the relevant libraries

# In[1]:


# For these lessons we will need NumPy, pandas, matplotlib and seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# and of course the actual regression (machine learning) module
from sklearn.linear_model import LinearRegression


# ## Load the data

# In[4]:


# Load the data from a .csv in the same folder
data = pd.read_csv("C:/Users/Praveen B Ronad/Downloads/real_estate_price_size_year (2).csv")

# Let's explore the top 5 rows of the df
data.head()


# In[5]:


data.describe()


# ## Create the regression

# ### Declare the dependent and the independent variables

# In[6]:


x = data[['size','year']]
y = data['price']


# ### Regression

# In[7]:


reg = LinearRegression()
reg.fit(x,y)


# ### Find the intercept

# In[10]:


reg.intercept_


# ### Find the coefficients

# In[11]:


reg.coef_


# ### Calculate the R-squared

# In[12]:


reg.score(x,y)


# ### Calculate the Adjusted R-squared

# In[ ]:


x.shape


# In[13]:


r2 = reg.score(x,y)
n = x.shape[0]
p = x.shape[1]

adjusted_r2 = 1-(1-r2)*(n-1)/(n-p-1)
adjusted_r2


# ### Compare the R-squared and the Adjusted R-squared

# Answer...

# ### Compare the Adjusted R-squared with the R-squared of the simple linear regression

# Answer...

# ### Making predictions
# 
# Find the predicted price of an apartment that has a size of 750 sq.ft. from 2009.

# In[20]:


predictions=reg.predict([[750,2009]])
predictions


# In[22]:


predictions=reg.predict([[1000,2016]])
predictions


# ### Calculate the univariate p-values of the variables

# In[23]:


from sklearn.feature_selection import f_regression


# In[25]:


f_regression(x,y)


# In[28]:


pvalue=f_regression(x,y)[1]
pvalue


# In[29]:


pvalue.round(3)


# ### Create a summary table with your findings

# In[30]:


reg_summary = pd.DataFrame(data = x.columns.values, columns=['Features'])
reg_summary ['Coefficients'] = reg.coef_
reg_summary ['p-values'] = pvalue.round(3)
reg_summary


# Answer...
