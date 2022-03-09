#!/usr/bin/env python
# coding: utf-8

# # Creating a logistic regression to predict absenteeism

# ### Import the relevent libraries 

# In[1]:


import numpy as np
import pandas as pd


# ### Load the preproccessed data
# 

# In[2]:


data_preprocessed=pd.read_csv("C:/Users/Praveen B Ronad/Downloads/Absenteeism_preprocessed.csv")


# In[3]:


data_preprocessed.head()


# In[4]:


# the model itself gives us fair indication of which variables are important for the analysis


# #### Create the targets 

# In[5]:


'''
Two classes 
moderatley absent 
excessively absent
we will take median value of absenteesium column
every value<= 3 is moderate  are assigned target 0
every value>= 4 is excessive absence are assigned target 1
median is 3
'''
data_preprocessed['Absenteeism Time in Hours'].median()


# In[6]:


#np.ehere(condtion,value if True,value if false) checks if condtion has been satisfied and assign a value accordingly

targets=np.where(data_preprocessed['Absenteeism Time in Hours']>data_preprocessed['Absenteeism Time in Hours'].median(),1,0)


# In[7]:


targets # is a np array


# In[8]:


data_preprocessed['Excessive Absenteeism']=targets
data_preprocessed


# #### Coment on the targets

# In[9]:


#Using the median as a cutoff line 'numerically stable and regid'
# by using median we implicitly balanced dataset
# this will prevent our model from learning to output only 0s and 1s

# Total number of targets which are 1s

targets.sum() 


# In[10]:


targets.sum()/targets.shape[0] # 46% of the targets are 1s  60-40 will work fro logistic regression


# Drop Absenteeism Time in Hours 

# In[11]:


data_with_targets=data_preprocessed.drop(['Absenteeism Time in Hours'],axis=1)


# In[12]:


data_with_targets.head()


# In[13]:


data_with_targets is data_preprocessed


# ### Select inputs for logistic regression
# > DataFrame.iloc[row indices,column_indices] Selects(slices) data by position when given rows and columns 

# In[14]:


# check the shape of dataframe
data_with_targets.shape


# In[15]:


data_with_targets.iloc[:,0:-1]


# In[16]:


unscaled_inputs=data_with_targets.iloc[:,:-1]


# In[17]:


unscaled_inputs


# #### standardize the data ( scaling)

# In[24]:


from sklearn.preprocessing import StandardScaler
absenteeism_scaler=StandardScaler()
absenteeism_scaler


# In[25]:


absenteeism_scaler.fit(unscaled_inputs)


# In[29]:


absenteeism_scaler.mean_


# In[34]:


unscaled_inputs # inputs are still unscaled , we have just prepared scaling mechanism


# In[37]:


# in order to apply scaling we need to use .transform
# . transform does the actual scaling
# whenever we get new data we just use absenteeism_scaler.transform(new data)
scaled_inputs=absenteeism_scaler.transform(unscaled_inputs)


# In[38]:


scaled_inputs


# In[39]:


scaled_inputs.shape


# ## spiting the data for training and testing
# > Train data set
# > Test data set
# > Shuffling 

# import revlent libraries 

# In[40]:


from sklearn.model_selection import train_test_split


# Split

# In[69]:


# sklearn.model_selection.train_test_split(inputs,targets,train_size,shuffle=False) splits arrays or matrices into train and test subset

train_test_split(scaled_inputs,targets)

'''
sklearn.model_selection.train_test_split(inputs,targets,train_size,shuffle=True)
Splits arrays or matrices into random train and test subset

output conatines 4 array

Array 1: a training data set with inputs
Array 2: A training data with targets 
Array 3: A test dataset with inputs
Array 4: A test data set with targets 
'''


# Delecare 4 variables conatining 4 outputs 

# In[70]:


x_train, x_test, y_train, y_test= train_test_split(scaled_inputs,targets,train_size=0.8,shuffle=True,random_state=20)
# random_state makes a shuffle pseduo random , the method will always shuffle the observation in the same 'random way'
# 0.9 is 90 % is training 
# 0.8 for 80% training 


# In[71]:


# see the shape of each variable

print(x_train.shape,y_train.shape)


# In[72]:


print(x_test.shape,y_test.shape)


# ## Logistic Regression with sklearn 

# ##### Training the Model
# > We use sklearn insted of stats model
# 

# In[73]:


from sklearn.linear_model import LogisticRegression
from sklearn import metrics


# training the model

# In[74]:


reg=LogisticRegression()


# In[75]:


reg.fit(x_train,y_train)
# .fit(input,output) does all the ML work and generates weights and biases


# In[86]:


# get the results 
reg.score(x_train,y_train)
# reg.score(inputs,targets) returns the mean accuracy on the given data and lables
# based on the data we used , our model learned to classify appriximaltly 80% of the observations correctly


# ### Manually check the accuracy 

# In[87]:


#sklearn.linear_model.LogisticRegression.predict(inputs) predicts the class lables (logistic regression outputs) for given samples
model_outputs=reg.predict(x_train)


# In[90]:


model_outputs


# In[91]:


# targets are stored in y_train data set
y_train


# In[92]:


model_outputs==y_train


# In[93]:


# How many values are True i.e 1
# True =1 False=0
np.sum(model_outputs==y_train)


# In[95]:


# get total numbers
model_outputs.shape[0]


# In[97]:


manual_accuracy=(np.sum(model_outputs==y_train)/model_outputs.shape[0])*100


# In[98]:


manual_accuracy


# ##### Creating a summary table with coeffcients and intercepts

# In[99]:


# find intercept
reg.intercept_


# In[100]:


# find coeff
reg.coef_


# In[101]:


scaled_inputs.columns.values # scaled inputs is not an panads dataframe so it gives error


# In[102]:


unscaled_inputs.columns.values


# In[103]:


feature_name=unscaled_inputs.columns.values


# In[110]:


# create a dataframe which conatins intercepts and weihts for all column

summary_table=pd.DataFrame(columns=['feature_name'],data=feature_name)
summary_table['Coefficient']=np.transpose(reg.coef_)


# In[111]:


summary_table


# In[ ]:




