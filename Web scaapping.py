#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import bs4
from bs4 import BeautifulSoup


# In[5]:


url="https://www.flipkart.com/clothing-and-accessories/~cs-3jd7c6dspk/pr?sid=clo&collection-tab-name=Men%27s+Clothing&p%5B%5D=facets.price_range.from%3D199&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.ideal_for%255B%255D%3DMen&offer=nb:mp:014a0b0923,nb:mp:01c6bfbe22,nb:mp:01cb82fe22&hpid=gV6EaKZt5Qwr5RLmkIGlLKp7_Hsxr70nj65vMAAFKlc=&fm=neo%2Fmerchandising&iid=M_20c72c00-2b05-44f4-8942-bca72f13fd94_4.IU83CFXRBA8H&ssid=n75wkoc39s0000001645691164808&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_4.dealCard.OMU_IU83CFXRBA8H_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_3&cid=IU83CFXRBA8H"


# In[8]:


headers={
    
    'User_Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
}


# In[9]:


r=requests.get(url,{'headers':headers})


# In[10]:


soup= bs4.BeautifulSoup(r.text,'html.parser')


# In[11]:


soup.find_all


# In[12]:


soup.find_all('div')


# In[ ]:




