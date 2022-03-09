#!/usr/bin/env python
# coding: utf-8

# ### Task : Predict Absenteeism from work

# In[1]:


import pandas as pd


# In[2]:


raw_csv_data=pd.read_csv("C:/Users/Praveen B Ronad/Downloads/Absenteeism_data (2).csv")


# In[3]:


raw_csv_data


# In[4]:


df=raw_csv_data.copy()
df


# In[5]:


# pd.options.display.max_columns = NONE displays all coulumns 
# pd.options.display.max_rowa =NONE displays all coulumns 
pd.options.display.max_columns=None
pd.options.display.max_rows=None


# In[6]:


df


# In[7]:


#df.info()-- Prints a consise summary of the data frame
df.info()


# In[8]:


# Absenteeism Time in Hours is our Dependant variable  , remaining are independant 


# Drop 'ID' Column from dataframe as it doesnot matter in analysis

# In[9]:


# Id is just a labe nominal data
## use object.drop([list]) which remove specified rows or column
df.drop(['ID'],axis=1)


# In[10]:


# check the content of the df dataframe
# ID column still there!
## .drop() delivers a temporary ouput
df


# In[11]:


df=df.drop(['ID'],axis=1)


# In[12]:


df


# # Reason for Absence 

# In[13]:


df['Reason for Absence']


# In[14]:


# to know max and min values use .min and .max function
df['Reason for Absence'].max()


# In[15]:


df['Reason for Absence'].min()


# In[16]:


# we want to extract a list conating distinct values only
# pd.unique() extracts distinct values only
pd.unique(df['Reason for Absence'])


# In[17]:


## 2nd method to obtain distinct values of a column
df['Reason for Absence'].unique()


# In[18]:


# len() returns the number of elements in an object
len(df['Reason for Absence'].unique())


# In[19]:


# A number between 0 and 28 is missing bx max is 28 min is 0 so tatal 29 
# but len() given 28 as an output
# how to find missing reason number ? Ans: Sorted
# Built in sorted() returns a new , sorted list from the items in its argument

sorted(df['Reason for Absence'].unique())

# missing reason number is 20


# .get_dummies()

# 
# '''
# >>which are the 28 reasons we have  substituted with numbers here?
# >>reason for Ab values are categorical nominal 
# >>Quantitave analysis: add numeric meaning to our catgorical nominal values ex 0,1,2,28
# 
# how can we convert:>> dummy variables 
# 
# Dummy Variables
# an explanatory binary variable that equals 
# 1 if a certain categorical effect is present , and that equal 
# 0 if that same effect is absent
# 
# Assumption: We can be certain that an individual has been absent from work because of one and only one , perticular reason
# 
# pd.get_dummies() >> Converts categorical variables into a dummy variables 0 and 1
# 
# '''
# 
# 

# In[20]:


reason_columns=pd.get_dummies(df['Reason for Absence'])


# In[21]:


reason_columns


# In[22]:


# check rows with missing values : create new col = check 
## if sum is 0: then there is a missing values 
## if sum is 1 : then there is only one value and that is 1 
## if sum is 2 or more : then 1 may be repeated or more number
reason_columns['Check']=reason_columns.sum(axis=1)
reason_columns


# In[23]:


# CHECK wehter all values of 'check' col are 1 or not by summing it it shiudl give values lenght  700
reason_columns['Check'].sum(axis=0)



# In[24]:


# use unique method # how to make sure all values are only 1 not more than 1
reason_columns['Check'].unique()


# In[25]:


## now remove check column from reason_column data frame , beacuse we confirmed 
## use .drop(['coulmn name'], axis=) method

reason_columns=reason_columns.drop(['Check'],axis=1)
reason_columns


# Drop reason 0 column 
# because we want to avoid multicolinerality issues
# 
# 

# In[26]:


reason_columns=pd.get_dummies(df['Reason for Absence'],drop_first=True)
reason_columns


# ## Classifying Various reasons for Absentees
# >>Group the reason for Absence 
# '''
# still reasons 1 to 28 are too many for analysis , so its better we group them into few reasons numbers
# '''
# 

# In[27]:


# get the columns headers in df
df.columns.values


# In[28]:


# get the coulmn headers in reason_columns
reason_columns.columns.values


# '''
# Three steps to take before finalising reason column
# **step 1:** id we decide to add all the dummy variables into df we would observe duplicate information
#         i,e 'reasons for absence' would convey same infolamtion as all 27 column from reason_columns
#         
#         this is called as " Multi-colineearity "---> it should be avoided 
#         
#         there fore we should drop ' reason for absence' coulumn from the df
# **step 2:**  Grouping the dummy  variables
# if we add all 27 reason column in df .. it will be having around 40 columns
# 
# Group
# 'reorganising certain type of variables into groups in a regression analysis called classifiaction'
# Group is also called as Class
# 
# Group 1: reason 1 to reason 14 --> Serious health condition
# Group 2: reason 15 to 17 --> pregancy and giving birth
# Group 3: reason 18-21--> poisoning 
# Group 4: reason 22-28--> light reasons 
# 
# **step 3:** 
# Concatenate Column Values 
# add reason_type_1 ,2,3,4 into df dataFrame 
# Use>> pd.concat()
# '''

# In[29]:


# Drop 'Reason for Absence' column from df
df=df.drop(['Reason for Absence'],axis=1)
df


# In[30]:


reason_columns.loc[:,'1':'14']


# In[31]:


reason_columns.loc[:,'1':'14'] # .loc[] is lable based not index based 
'''
Reason_1
0: NONE of the values on the given row were equal to 1
1: somehere amoung these 14 columns we have observeed the number 1 
.max() returns highst value

'''


# In[32]:


reason_columns.loc[:,21:]


# In[33]:


reason_type_1=reason_columns.loc[:,'1':'14'].max(axis=1)
# obtained object is pandas series not a dataframe
# we can insert this column in df DataFrame 
# do simliarly for other groups
reason_type_2=reason_columns.loc[:,'15':'17'].max(axis=1)
reason_type_3=reason_columns.loc[:,'18':'21'].max(axis=1)
reason_type_4=reason_columns.loc[:,'22':].max(axis=1)


# In[34]:


reason_type_4


# In[35]:


reason_columns.loc[:,15:'17']


# In[36]:


# Create new dataframe for each Group 
# After spliting reason_columns object into smaller pieces each piece itself will be DataFrame as well
# .loc[:,] retrive all rows avalable .loc[] is lable based 
#reason_type_1=reason_columns.loc[].max(axis=1)


# Concatenate the column values

# In[37]:


df=pd.concat([df,reason_type_1,reason_type_2,reason_type_3,reason_type_4],axis=1)


# In[38]:


df


# In[39]:


# 4 columns added at the last 
# change the column name 0,1,2,3
df.columns.values


# In[40]:


column_names=['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours', 'reason_1', 'reason_2', 'reason_3', 'reason_4']


# In[41]:


# to assign new column values in a data frame
df.columns=column_names


# In[42]:


df.head()


# Reorder the Columns
# 
# > create another list with column name 
# > column_names_reordered

# In[43]:


column_names_reordered=['reason_1', 'reason_2', 'reason_3', 'reason_4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[44]:


df=df[column_names_reordered]


# In[45]:


df.head()


# #### Creating a checkpoint
# > Checkpoints is an interim save of your work
# >> In programming in gen , and in Jupyter in perticuluer , creating checkpoints refers to storing the current version of your code, not really the content of a variable

# ###### check point

# In[46]:


# create a copy of the current state of df DataFrame
df_reason_mod=df.copy()


# In[47]:


df_reason_mod


# ### Analaysis of Date Column

# In[48]:


df_reason_mod['Date'] # evvery column is a pandas series object
## dd/mm/yyyy


# In[50]:


type(df_reason_mod['Date'])


# In[56]:


# check type of values in date column
type(df_reason_mod['Date'][0])
# Now Dates values are stores as String datatypes


# ##### Time stamp
# > A classical data type found in many programming langauges out there, used for values represeting date and time
# >> pd.to_datetime() converts values into timestamp
# >>> We mus specfiy proper date format 

# In[57]:


df_reason_mod['Date']=pd.to_datetime(df_reason_mod['Date'])


# In[58]:


df_reason_mod['Date']


# In[59]:


'''
use format parameter 
format='string' alllows you to take control over how pythin will read the current dates,
so that it can accurately understand which numbers referes to date , month,years,hrs,minu,seconds
>> String will not designiate the format of timestamp you are about to create
%d--> day
%m--> month
%Y--> year( has to be uppercase)

%H--> Hour
%M--> Minute(uppper case)
%S--> seconds(uppercase)

'''
df_reason_mod['Date']=pd.to_datetime(df_reason_mod['Date'],format='%d%m%Y')


# In[61]:


df_reason_mod['Date'] # Standared timestamp format yyyy-mm-dd


# In[62]:


type(df_reason_mod['Date']) # now values in date columns are not 'strings' they are timestamp 


# In[63]:


type(df_reason_mod['Date'][0])


# In[64]:


# use .info() method to see overview
df_reason_mod.info()


# ##### extracting a month value from ['Date'] column

# In[68]:


df_reason_mod['Date'][0]
# time stmp conatin two parts date and time


# In[69]:


# to extract month value only use .month
df_reason_mod['Date'][0].month


# In[70]:


# to extract day value only use .day
df_reason_mod['Date'][0].day


# In[71]:


# to extract year value only use .year
df_reason_mod['Date'][0].year


# In[90]:


df_reason_mod.shape[0]


# In[91]:


# create list of months 
#add list to data frame
# more sofasticated way to write for loop
# .shape gives two values  first - lengh and second - width
#df_reason_mod.shape[0] gives 700 value for this dataframe

list_months=[]
for i in range(df_reason_mod.shape[0]):
    list_months.append(df_reason_mod['Date'][i].month)
    


# In[92]:


list_months


# In[93]:


len(list_months)


# In[94]:


# check type of list
type(list_months)


# In[95]:


# add this list to data frame df_reason_mod

df_reason_mod['Month Value']=list_months


# In[96]:


df_reason_mod


# In[97]:


# see only first 10 rows
df_reason_mod.head(10)


# #### extracting day of the week

# In[101]:


# .weekday returns an integer corresponding to the day of the week
'''
0-Mon , 1-Tue, 2-Wed, 3-thu, 4-fri, 5-sat, 6-sun

'''
df_reason_mod['Date'][699].weekday()


# In[105]:


'''
to apply c certain type of odifiaction iteratively on each values
- from  aseries or a column in a dataframe , it is agreat idea to create a function 
that can excecute this operation for one element, and then impleiment it to alll values from column of intrest

'''
def date_to_weekday(date_value):
    return date_value.weekday()


# In[106]:


df_reason_mod['Day of the Week']=df_reason_mod['Date'].apply(date_to_weekday)


# In[114]:


df_reason_mod.head(2)


# ###### Drop date column from the df_reason_mod

# In[127]:


df_reason_mod=df_reason_mod.drop(['Date'],axis=1)


# In[128]:


df_reason_mod.head(1)


# In[129]:


# to get the column header name use .columns.values
df_reason_mod.columns.values


# In[130]:


list_ordered_date=['reason_1', 'reason_2', 'reason_3', 'reason_4','Month Value',
       'Day of the Week',
       'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours' ]


# In[131]:


df_reason_mod=df_reason_mod[list_ordered_date]


# In[132]:


df_reason_mod.head(2)


# ### create check point df_reason_date_mod

# In[133]:


df_reason_date_mod=df_reason_mod.copy()


# In[135]:


# check the type of monthly transportaion ecpenses in dollers 
type(df_reason_date_mod['Transportation Expense'][0])


# In[136]:


# check the type of Age
type(df_reason_date_mod['Age'][0])


# In[138]:


# check the type of Distance to Work in km
type(df_reason_date_mod['Distance to Work'][0])


# In[139]:


# check the type ofDaily Work Load Average- the avg amount of time spent working per day, shown in minutes
type(df_reason_date_mod['Daily Work Load Average'][0])


# #### Education,children and pets

# In[140]:


# display method 
display(df_reason_date_mod)


# In[141]:


# find unique education categories
df_reason_date_mod['Education'].unique()


# In[142]:


'''
there are four unique categories eduaction 1,2,3,4
above number dont have meaning 
1- high School edu----> 0
2- Gradu
3- post graduate
4- a master or a doctor

2,3,4 as --> each 1
'''
df_reason_date_mod['Education'].value_counts() # returns the number times of 1's 2's 3's and 4's


# In[145]:


#around 583 are high school , remaining are can be grouped into one category
# use .map({dict}) 

df_reason_date_mod['Education']=df_reason_date_mod['Education'].map({1:0,2:1,3:1,4:1})


# In[146]:


# count how many distinct values are present 

df_reason_date_mod['Education'].unique()


# In[148]:


df_reason_date_mod['Education'].value_counts()


# #### Final Checkpoint

# In[150]:


df_preprocessed=df_reason_date_mod.copy()
df_preprocessed


# In[151]:




df_preprocessed=df_preprocessed.to_csv('C:/Users/Praveen B Ronad/Downloads/Absenteeism_preprocessed.csv', index=False)


# In[ ]:




