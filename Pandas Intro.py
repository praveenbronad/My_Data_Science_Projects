#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd


# In[12]:


data=pd.Series([2,3,4,5,6,7])
data


# In[5]:


data.values


# In[8]:


data.index


# In[18]:


data[0:2]


# In[26]:


info=pd.Series([545,'praveen','mech',8,2016],index=['id','name','dept','exp','doj'])
info


# In[28]:


info['id']


# In[29]:


eng_dict={'mech':300,'cse':500,'ece':400}
eng_dict


# In[30]:


NumOfStudents=pd.Series(eng_dict)
NumOfStudents


# In[31]:


NumOfStudents['mech']


# In[37]:


NumOfStudents['mech':'ece']


# In[41]:


NumOfStudents.mean()


# In[42]:


stu=pd.Series({'mech':300,'cse':500,'ece':400},index=['mech','ece'])
stu


# In[44]:


population_dict = {'California': 38332521,
 'Texas': 26448193,
 'New York': 19651127,
 'Florida': 19552860,
 'Illinois': 12882135}
population = pd.Series(population_dict)
population


# In[47]:


area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
 'Florida': 170312, 'Illinois': 149995}
area_dict
area=pd.Series(area_dict)
area


# In[52]:


states = pd.DataFrame({'population': population,
 'area': area })
states


# In[53]:


states.index


# In[55]:


states.columns


# In[62]:


states['population']


# In[5]:


import pandas as pd
data = [{'a': i, 'b': 2 * i}
 for i in range(5)]
pd.DataFrame(data)
data


# In[6]:


print(pd.DataFrame(data))


# In[8]:


import numpy as np
pd.DataFrame(np.random.rand(3, 2),
 columns=['foo', 'bar'],
 index=['a', 'b', 'c'])


# In[ ]:




