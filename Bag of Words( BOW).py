#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


paragraph="""
Dr. Kalam was one of the most important figures in the testing of the Pokhran-II in the year 1988. Politics never attracted Dr. Kalam. But in the year 2002, Indian National Democratic Alliance requested him to nominate him for the post of the President. Thinking of the nation and keen eagerness to work for the country, made him say yes. With the support of the Indian National Democratic Alliance, he won the elections and was selected as the President of India.Dr. Kalam was one of the most important figures in the testing of the Pokhran-II in the year 1988. Politics never attracted Dr. Kalam. But in the year 2002, Indian National Democratic Alliance requested him to nominate him for the post of the President. Thinking of the nation and keen eagerness to work for the country, made him say yes. With the support of the Indian National Democratic Alliance, he won the elections and was selected as the President of India. Dr. Kalam was one of the most important figures in the testing of the Pokhran-II in the year 1988. Politics never attracted Dr. Kalam. But in the year 2002, Indian National Democratic Alliance requested him to nominate him for the post of the President. Thinking of the nation and keen eagerness to work for the country, made him say yes. With the support of the Indian National Democratic Alliance, he won the elections and was selected as the President of India.



"""


# In[3]:


import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


# In[12]:


ps= PorterStemmer()
#wordnet= WordNetLemmatizer()
sentences =nltk.sent_tokenize(paragraph)
corpus= []
for i in range(len(sentences)):
    review= re.sub('[^a-zA-z]', ' ', sentences[i])
    review= review.lower()
    review= review.split()
    review= [ps.stem(word)for word in review if not word in set(stopwords.words('english'))]
    review= ' '.join(review)
    corpus.append(review)


# In[13]:


sentences


# In[14]:


corpus # with stemming


# In[15]:


# creating the bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
X=cv.fit_transform(corpus).toarray()


# In[16]:


X # with stemming


# In[21]:


# with lammaitizer
wordnet= WordNetLemmatizer()
sentences =nltk.sent_tokenize(paragraph)
corpus= []
for i in range(len(sentences)):
    review= re.sub('[^a-zA-z]', ' ', sentences[i])
    review= review.lower()
    review= review.split()
    review= [wordnet.lemmatize(word)for word in review if not word in set(stopwords.words('english'))]
    review= ' '.join(review)
    corpus.append(review)
# creating the bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
X=cv.fit_transform(corpus).toarray()


# In[22]:


sentences


# In[23]:


corpus


# In[24]:


X


# In[ ]:




