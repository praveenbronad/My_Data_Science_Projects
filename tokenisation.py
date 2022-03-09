#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


nltk.download()


# In[5]:


paragraph="""
Input refers to the electronic information required to describe the physical object with 3D data. 
There are two possible starting points a computer model or a physical model. The computer 
model created by a CAD system can be either a surface model or a solid model. On the other 
hand, 3D data from the physical model is not at all straightforward. It requires data acquisition 
through a method known as reverse engineering. In reverse engineering, a wide range of 
equipment can be used, such as CMM (coordinate measuring machine) or a laser digitizer, to 
capture data points of the physical model and “reconstruct” it in a CAD system.

"""


# In[6]:


nltk.sent_tokenize(paragraph)


# In[7]:


len(nltk.sent_tokenize(paragraph))


# In[ ]:




