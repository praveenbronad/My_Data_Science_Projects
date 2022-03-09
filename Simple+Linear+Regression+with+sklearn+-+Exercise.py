#!/usr/bin/env python
# coding: utf-8

# # Simple linear regression - Exercise

# You are given a real estate dataset. 
# 
# Real estate is one of those examples that every regression course goes through as it is extremely easy to understand and there is a (almost always) certain causal relationship to be found.
# 
# The data is located in the file: 'real_estate_price_size.csv'. 
# 
# You are expected to create a simple linear regression (similar to the one in the lecture), using the new data. 
# 
# Apart from that, please:
# -  Create a scatter plot (with or without a regression line)
# -  Calculate the R-squared
# -  Display the intercept and coefficient(s)
# -  Using the model make a prediction about an apartment with size 750 sq.ft.
# 
# Note: In this exercise, the dependent variable is 'price', while the independent variable is 'size'.
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


# We start by loading the data
data = pd.read_csv("C:/Users/Praveen B Ronad/Downloads/real_estate_price_size (1).csv")

# Let's explore the top 5 rows of the df
data.head()


# In[9]:


x=data['size']
y=data['price']


# ## Create the regression

# ### Declare the dependent and the independent variables

# In[28]:


# In order to feed x to sklearn, it should be a 2D array (a matrix)
# Therefore, we must reshape it 
# Note that this will not be needed when we've got more than 1 feature (as the inputs will be a 2D array by default)

# x_matrix = x.values.reshape(84,1)
x_matrix = x.values.reshape(-1,1)

# Check the shape just in case
x_matrix.shape


# In[29]:


plt.scatter(x,y)
plt.xlabel('Size',fontsize=20)
plt.ylabel('Price',fontsize=20)
plt.show()


# ### Explore the data

# ### Regression itself

# In[30]:


reg = LinearRegression()
reg.fit(x_matrix,y)


# ### Calculate the R-squared

# In[31]:


reg.score(x_matrix,y)


# ### Find the intercept

# In[32]:


reg.intercept_


# ### Find the coefficients

# In[24]:


reg.coef_


# ### Making predictions
# 
# You find an apartment online with a size of 750 sq.ft.
# 
# All else equal what should be its price according to the model?

# In[37]:


predictions=reg.predict( [[ 750 ],[1000]] )
predictions


# In[ ]:





# In[ ]:




