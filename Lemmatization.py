#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords 


# In[2]:


paragraph ="""
In the SLA, a laser beam with a specified power and wavelength is sent through a beam 
expanding telescope to fill the optical aperture of a pair of cross axis, galvanometer driven, and 
beam scanning mirrors. These form the optical scanning system of the SLA. The beam comes to 
a focus on the surface of a liquid photopolymer, curing a predetermined depth of the resin after 
a controlled time of exposure (inversely proportional to the laser scanning speed). The 
solidification of the liquid resin depends on the energy per unit area (or “exposure”) deposited 
during the motion of the focused spot on the surface of the photopolymer. There is a threshold 
exposure that must be exceeded for the photopolymer to solidify.
"""


# In[3]:



sentences= nltk.sent_tokenize(paragraph)
lemmatizer= WordNetLemmatizer()


# In[4]:


# Lemmatizataion
for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words= [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('English'))]
    sentences[i]= ' '.join(words)


# In[5]:


sentences


# In[ ]:




