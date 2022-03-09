#!/usr/bin/env python
# coding: utf-8

# # Multiple Linear Regression with Dummies - Exercise

# You are given a real estate dataset. 
# 
# Real estate is one of those examples that every regression course goes through as it is extremely easy to understand and there is a (almost always) certain causal relationship to be found.
# 
# The data is located in the file: 'real_estate_price_size_year_view.csv'. 
# 
# You are expected to create a multiple linear regression (similar to the one in the lecture), using the new data. 
# 
# In this exercise, the dependent variable is 'price', while the independent variables are 'size', 'year', and 'view'.
# 
# #### Regarding the 'view' variable:
# There are two options: 'Sea view' and 'No sea view'. You are expected to create a dummy variable for view and include it in the regression
# 
# Good luck!

# ## Import the relevant libraries

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
# We can override the default matplotlib styles with those of Seaborn
sns.set()


# ## Load the data

# In[8]:


# Load the data from a .csv in the same folder. Since we will do some preprocessing, the variable is not called 'data' just yet!
raw_data = pd.read_csv("C:/Users/Praveen B Ronad/Downloads/real_estate_price_size_year_view.csv")


# In[9]:


raw_data


# In[38]:


data=raw_data.copy()
data
data['view']=data['view'].map({'Sea view':1,'No sea view':0})
data.describe()


# ## Create a dummy variable for 'view'

# In[ ]:





# In[ ]:





# ## Create the regression

# ### Declare the dependent and the independent variables

# In[35]:


y=data['price']
x1=data[['size','year','view']]


# ### Regression

# In[36]:


# Add a constant. Esentially, we are adding a new column (equal in lenght to x), which consists only of 1s
x = sm.add_constant(x1)
# Fit the model, according to the OLS (ordinary least squares) method with a dependent variable y and an idependent x
results = sm.OLS(y,x).fit()
# Print a nice summary of the regression.
results.summary()


# Plot the regression line(s) on the scatter plot

# In[43]:


# Create a scatter plot of size and price
plt.scatter(data['size'],y)
# Define the two regression equations, depending on whether they sea view (yes), or no sea view (no)
yhat_yes=-5.398e+06+218.7521*data['size']+2718.9489*data['year']+5.673e+04
yhat_no = -5.398e+06+218.7521*data['size']+2718.9489*data['year']
# Plot the two regression lines
fig = plt.plot(data['size'],yhat_no, lw=0.5, c='#006837')
fig = plt.plot(data['size'],yhat_yes, lw=0.5, c='#a50026')
# Name your axes :)
plt.xlabel('size', fontsize = 20)
plt.ylabel('price', fontsize = 20)
plt.show()


# In[ ]:




