#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from nltk import PorterStemmer
from nltk.corpus import stopwords


# In[3]:


paragraph="""
Input refers to the electronic information required to describe the physical object with 3D data. 
There are two possible starting points a computer model or a physical model. The computer 
model created by a CAD system can be either a surface model or a solid model. On the other 
hand, 3D data from the physical model is not at all straightforward. It requires data acquisition 
through a method known as reverse engineering. In reverse engineering, a wide range of 
equipment can be used, such as CMM (coordinate measuring machine) or a laser digitizer, to 
capture data points of the physical model and “reconstruct” it in a CAD system.
"""


# In[4]:


len(paragraph)


# In[5]:


# COnvert paragraph into sentances 
sentances= nltk.sent_tokenize(paragraph)


# In[6]:


sentances


# In[7]:


len(sentances)


# In[14]:


stopwords.words('english')
len(stopwords.words('english'))


# In[15]:


stopwords.words('english')


# In[20]:


stopwords.words('french')


# In[8]:


stemmer= PorterStemmer()


# In[22]:


# Stemming
for i in range(len(sentances)):
    words=nltk.word_tokenize(sentances[i])
    words= [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentances[i]= ' '.join(words)


# In[23]:


sentances


# In[ ]:




