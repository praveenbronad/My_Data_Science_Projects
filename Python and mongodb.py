#!/usr/bin/env python
# coding: utf-8

# import pymongo

# In[1]:


import pymongo


# In[2]:


client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')


# In[3]:


#creating a database
mydb=client['Employee'] # if it is a new data base ,it will not be visible in mongodb  compas 


# In[4]:


# add collections 

information=mydb.employeeinformation


# In[5]:


# all the documents will be sttored as JSON 

records={
    
    "Firstname":"Praveen",
    "lastname":"ronad",
    "Department":"Mech"
    
    }


# In[6]:



information.insert_one(records) # insert_one adds only one document


# In[7]:


# Create multiple documents 

records=[
        {"Firstname":"Praveen",
           "lastname":"ronad",
            "Department":"Mech",
            "qual":["mtech","be"],
             "age":32
         },
      {
       "Firstname":"Sujata",
    "lastname":"G",
    "Department":"Bio",
          "qual":"bsc",
          "age":25
       },
     {
       "Firstname":"Abhi",
    "lastname":"masr",
    "Department":"mech",
         "qual":["mtech","be"],
         "age":34
       }
    
    ]


# In[8]:


information.insert_many(records)


# In[9]:


# Simple way of query
information.find_one() # returns top 1 record


# In[10]:


# all records
information.find() #returns cursor


# In[11]:


for record in information.find():
    print(record)


# In[12]:


# other way to get all the records
information.find({}) 


# In[13]:


for record in information.find({}):
    print(record)


# In[14]:


# query the json documents based on equality condtions
# Select * from information where first name =praveen
for record in information.find({"Firstname":"Praveen"}):
    print(record)


# In[15]:


## query documents using query operators ($in,$lt,$gt)
for record in information.find({"qual":{"$in":["mtech","be"]}}):
    print(records)


# In[20]:


## and and query 
for record in information.find({"qual":"mtech","age":{"$lt":35}}):
    print(record)


# In[23]:


## or operator $or
for record in information.find({"$and":[{"Firstname":"Praveen"},{"qual":"be"}]}):
                                       print(record)


# In[24]:





# In[ ]:




