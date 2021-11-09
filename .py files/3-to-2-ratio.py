#!/usr/bin/env python
# coding: utf-8

# # Question-4 (3-to-2-ratio)

# In[2]:


# loading necessary libraries
import numpy as np
import pandas as pd


# In[3]:


state_code = []
state_name = []
three_to_two_ratio = []



for i in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(i)+"00.XLSX",header=5)
    
    c = ['State_Code','State_Name','Main_Ln_Code','main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    y = list(a['State_Code'].dropna().unique())
    state_code.append(("{:02d}".format(y[0])))
    state_name.extend(list(a['State_Name'].dropna().unique()))
    
    unique_Main_Ln = list(a['Main_Ln_Code'].dropna().unique())
    list_of_index_Main_Ln = []
    for i in unique_Main_Ln:
        list_of_index_Main_Ln.extend(a.index[a['Main_Ln_Code']==i].tolist())
    total_person_Main_Ln = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln = total_person_Main_Ln + a['Main_Ln_Persons'][i]
    
    
    unique_1st_Sub_Ln = list(a['1st_Sub_Ln_Code'].dropna().unique())
    list_of_index_1st_Sub_Ln = []
    for i in unique_1st_Sub_Ln:
        list_of_index_1st_Sub_Ln.extend(a.index[a['1st_Sub_Ln_Code']==i].tolist())
    total_person_1st_Sub_Ln = 0
    for i in list_of_index_1st_Sub_Ln:
        total_person_1st_Sub_Ln = total_person_1st_Sub_Ln + a['1st_Sub_Ln_Persons'][i]
    
    
    unique_2nd_Sub_Ln = list(a['2nd_Sub_Ln_Code'].dropna().unique())
    list_of_index_2nd_Sub_Ln = []
    for i in unique_2nd_Sub_Ln:
        list_of_index_2nd_Sub_Ln.extend(a.index[a['2nd_Sub_Ln_Code']==i].tolist())
    total_person_2nd_Sub_Ln = 0
    for i in list_of_index_2nd_Sub_Ln:
        total_person_2nd_Sub_Ln = total_person_2nd_Sub_Ln + a['2nd_Sub_Ln_Persons'][i]
    
    three_to_two_ratio.append(total_person_2nd_Sub_Ln/(total_person_1st_Sub_Ln-total_person_2nd_Sub_Ln))
    
    
    
    
for i in range(10,36):
    a = pd.read_excel("DDW-C17-"+str(i)+"00.XLSX",header=5)
    c = ['State_Code','State_Name','Main_Ln_Code','main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    # for state code
    state_code.extend(list(a['State_Code'].dropna().unique()))
    state_name.extend(list(a['State_Name'].dropna().unique()))
    
    # for one language
    unique_Main_Ln = list(a['Main_Ln_Code'].dropna().unique())
    list_of_index_Main_Ln = []
    for i in unique_Main_Ln:
        list_of_index_Main_Ln.extend(a.index[a['Main_Ln_Code']==i].tolist())
    total_person_Main_Ln = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln = total_person_Main_Ln + a['Main_Ln_Persons'][i]
    
    
    #for first subsidiary language
    unique_1st_Sub_Ln = list(a['1st_Sub_Ln_Code'].dropna().unique())
    list_of_index_1st_Sub_Ln = []
    for i in unique_1st_Sub_Ln:
        list_of_index_1st_Sub_Ln.extend(a.index[a['1st_Sub_Ln_Code']==i].tolist())
    total_person_1st_Sub_Ln = 0
    for i in list_of_index_1st_Sub_Ln:
        total_person_1st_Sub_Ln = total_person_1st_Sub_Ln + a['1st_Sub_Ln_Persons'][i]
    
    
    # for second subsidiary langauge
    unique_2nd_Sub_Ln = list(a['2nd_Sub_Ln_Code'].dropna().unique())
    list_of_index_2nd_Sub_Ln = []
    for i in unique_2nd_Sub_Ln:
        list_of_index_2nd_Sub_Ln.extend(a.index[a['2nd_Sub_Ln_Code']==i].tolist())
    total_person_2nd_Sub_Ln = 0
    for i in list_of_index_2nd_Sub_Ln:
        total_person_2nd_Sub_Ln = total_person_2nd_Sub_Ln + a['2nd_Sub_Ln_Persons'][i]
        
    three_to_two_ratio.append(total_person_2nd_Sub_Ln/(total_person_1st_Sub_Ln-total_person_2nd_Sub_Ln))


# In[8]:


# creating dataframe
df = pd.DataFrame({'state-code':state_code,'state-name':state_name,'3-to-2-ratio':three_to_two_ratio})
df


# In[9]:


# if we export csv from here state code 1 to 9 will be 1,2,3,4,5,6,7,8,9; not in 01,02,03,...09 format
# making state_code in proper format (for 01, previously it was 1, now it is '01')
df['state-code']=df['state-code'].apply('="{}"'.format)
df


# In[10]:


# sorting ratios to get states with top 3 and lowest 3 ratios
df.sort_values(by='3-to-2-ratio',ascending=False,inplace=True)
df


# In[16]:


# extracting states with top 3 and lowest 3 ratios
d1=df.head(3)
d2=df.tail(3)


# In[17]:


# making dataframe d2 in lower to higher ratio
d2.sort_values(by='3-to-2-ratio',inplace=True)
d2


# In[18]:


df1=pd.concat([d1,d2])
df1


# In[19]:


# exporting to csv
df1.to_csv("3-to-2-ratio.csv",index=False)


# In[ ]:





# In[ ]:





# In[ ]:




