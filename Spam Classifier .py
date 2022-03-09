#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import the data set 
import pandas as pd
messages = pd.read_csv('C:/Users/Praveen B Ronad/Downloads/smsspamcollection/SMSSpamCollection', sep='\t',names=['label','message'])


# In[4]:


# check messages data base
messages.head()


# In[16]:


print(messages['message'][0])
print(messages['message'][1])
print(messages['message'][2])
print(messages['message'][3])


# In[6]:


# import relevent libraries 
import re # re is regular expression library
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords # removes (the,that,am,there,at , etc)
from nltk.stem.porter import PorterStemmer # Stemming ( returns base value of a word)


# In[8]:


# check the stopwords in english langauge 
stopwords.words('english')


# In[17]:


ps=PorterStemmer()
corpus=[]
for i in range(0,len(messages)):
    review= re.sub('[^a-zA-Z]', ' ', messages['message'][i]) # sun method places all charactorts other than (!,.?& etc) ^ is not symbol
    review= review.lower()
    review= review.split()
    review= [ps.stem(word) 
             for word in review 
             if not word in stopwords.words('english')]
    review= ' '.join(review)
    corpus.append(review)
    


# In[19]:


messages


# In[20]:


corpus


# In[21]:


# creating the Bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=2500)
X=cv.fit_transform(corpus).toarray()


# In[28]:


## Input features and Taget feture 
X
y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values
y


# In[36]:


# splitiing data set into train and test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2, random_state=0,shuffle=True)


# In[37]:


# training model using Naive bayes classifier
from sklearn.naive_bayes import MultinomialNB
spam_detect_model=MultinomialNB().fit(X_train,y_train)


# In[38]:


y_pred=spam_detect_model.predict(X_test)


# In[39]:


y_pred


# In[40]:


from sklearn.metrics import confusion_matrix
confusion_m= confusion_matrix(y_test,y_pred)
confusion_m
# diagonal elements 946 and 153 are correctly predicted 
# 9,7 are wrongly predicted 
# total number of correct predictions are 946+153
# Total number of worng predictions are 9+7


# In[41]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[ ]:





# In[ ]:




