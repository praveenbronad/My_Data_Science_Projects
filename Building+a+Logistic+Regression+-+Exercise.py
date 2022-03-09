#!/usr/bin/env python
# coding: utf-8

# # Building a Logistic Regression

# Create a logistic regression based on the bank data provided. 
# 
# The data is based on the marketing campaign efforts of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit (variable y).
# 
# Note that the first column of the dataset is the index.
# 
# Source: [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014
# 

# ## Import the relevant libraries

# In[17]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Apply a fix to the statsmodels library
#from scipy import stats
#stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)


# ## Load the data

# Load the ‘Example_bank_data.csv’ dataset.

# In[18]:


raw_data = pd.read_csv("C:/Users/Praveen B Ronad/Downloads/Example_bank_data.csv")
raw_data


# We want to know whether the bank marketing strategy was successful, so we need to transform the outcome variable into 0s and 1s in order to perform a logistic regression.

# In[20]:


data = raw_data.copy()
data = data.drop(['Unnamed: 0'], axis = 1)
data['y'] = data['y'].map({'yes':1,'no':0})
data


# In[21]:


data.describe()


# ### Declare the dependent and independent variables

# In[22]:


y = data['y']
x1 = data['duration']


# ### Simple Logistic Regression

# Run the regression and visualize it on a scatter plot (no need to plot the line).

# In[23]:


x = sm.add_constant(x1)
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()
results_log


# In[25]:


results_log.summary()


# In[26]:


# Create a scatter plot of x1 (Duration, no constant) and y (Subscribed)
plt.scatter(x1,y,color = 'C0')

# Don't forget to label your axes!
plt.xlabel('Duration', fontsize = 20)
plt.ylabel('Subscription', fontsize = 20)
plt.show()


# In[ ]:




