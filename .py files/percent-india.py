#!/usr/bin/env python
# coding: utf-8

# In[1]:


# loading necessary libraries
import numpy as np
import pandas as pd


# In[2]:


# loading dataset
data_INDIA =pd.read_excel("DDW-C17-0000.XLSX",header=5)


# In[3]:


# to show first five rows
data_INDIA.head()


# In[4]:


# renaming columns and show the dataset
c = ['State_Code','State_Name','Main_Ln_Code','main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
data_INDIA.columns = c
data_INDIA


# In[5]:


# lenth of dataset
len(data_INDIA)


# In[6]:


# calculation total population in India, as each will have one unique mother toungue, sum of all people from mother toungue will produce total population in India
l=list(data_INDIA['Main_Ln_Code'].dropna().unique())
list_of_index = []
for i in l:
    list_of_index.extend(data_INDIA.index[data_INDIA['Main_Ln_Code']==i].tolist())
total_person = 0
for i in list_of_index:
    total_person = total_person + data_INDIA['Main_Ln_Persons'][i]
total_person


# In[7]:


# calculating total population having second language
l=list(data_INDIA['1st_Sub_Ln_Code'].dropna().unique())
list_of_index = []
for i in l:
    list_of_index.extend(data_INDIA.index[data_INDIA['1st_Sub_Ln_Code']==i].tolist())
total_person_1st_Sub = 0
for i in list_of_index:
    total_person_1st_Sub = total_person_1st_Sub + data_INDIA['1st_Sub_Ln_Persons'][i]
total_person_1st_Sub


# In[8]:


# calculating total population having third language
l=list(data_INDIA['2nd_Sub_Ln_Code'].dropna().unique())
list_of_index = []
for i in l:
    list_of_index.extend(data_INDIA.index[data_INDIA['2nd_Sub_Ln_Code']==i].tolist())
total_person_2nd_Sub = 0
for i in list_of_index:
    total_person_2nd_Sub = total_person_2nd_Sub + data_INDIA['2nd_Sub_Ln_Persons'][i]
total_person_2nd_Sub


# In[9]:


# calculate required columns of output file

state_code = []
percent_one = []
percent_two = []
percent_three = []


# for first 9 datasets having "DDW-C17-0i00.XLSX" format, i is from 1 to 9
for i in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(i)+"00.XLSX",header=5)
    #print(list_of_states[i])
    c = ['State_Code','State_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    y = list(a['State_Code'].dropna().unique())
    state_code.append(("{:02d}".format(y[0])))
    
    unique_Main_Ln = list(a['Main_Ln_Code'].dropna().unique())
    list_of_index_Main_Ln = []
    for i in unique_Main_Ln:
        list_of_index_Main_Ln.extend(a.index[a['Main_Ln_Code']==i].tolist())
    total_person_Main_Ln = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln = total_person_Main_Ln + a['Main_Ln_Persons'][i]
    #total_person_Main_Ln.append(s1)
    
    unique_1st_Sub_Ln = list(a['1st_Sub_Ln_Code'].dropna().unique())
    list_of_index_1st_Sub_Ln = []
    for i in unique_1st_Sub_Ln:
        list_of_index_1st_Sub_Ln.extend(a.index[a['1st_Sub_Ln_Code']==i].tolist())
    total_person_1st_Sub_Ln = 0
    for i in list_of_index_1st_Sub_Ln:
        total_person_1st_Sub_Ln = total_person_1st_Sub_Ln + a['1st_Sub_Ln_Persons'][i]
    #total_person_1st_Sub_Ln.append(s2)
    
    unique_2nd_Sub_Ln = list(a['2nd_Sub_Ln_Code'].dropna().unique())
    list_of_index_2nd_Sub_Ln = []
    for i in unique_2nd_Sub_Ln:
        list_of_index_2nd_Sub_Ln.extend(a.index[a['2nd_Sub_Ln_Code']==i].tolist())
    total_person_2nd_Sub_Ln = 0
    for i in list_of_index_2nd_Sub_Ln:
        total_person_2nd_Sub_Ln = total_person_2nd_Sub_Ln + a['2nd_Sub_Ln_Persons'][i]
    #total_person_2nd_Sub_Ln.append(s3)
    
    percent_one.append(((total_person_Main_Ln-total_person_1st_Sub_Ln)/total_person)*100)
    percent_two.append(((total_person_1st_Sub_Ln-total_person_2nd_Sub_Ln)/total_person)*100)
    percent_three.append((total_person_2nd_Sub_Ln/total_person)*100)
    
    
    
# for remaining datasets having "DDW-C17-i00.XLSX" format, i is from 10 to 35    
for i in range(10,36):
    a = pd.read_excel("DDW-C17-"+str(i)+"00.XLSX",header=5)
    #print(list_of_states[i])
    c = ['State_Code','State_Name','Main_Ln_Code','main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    # for state code
    state_code.extend(list(a['State_Code'].dropna().unique()))
    
    # for main language
    unique_Main_Ln = list(a['Main_Ln_Code'].dropna().unique())
    list_of_index_Main_Ln = []
    for i in unique_Main_Ln:
        list_of_index_Main_Ln.extend(a.index[a['Main_Ln_Code']==i].tolist())
    total_person_Main_Ln = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln = total_person_Main_Ln + a['Main_Ln_Persons'][i]
    #total_person_Main_Ln.append(s1)
    
    #for first subsidiary language
    unique_1st_Sub_Ln = list(a['1st_Sub_Ln_Code'].dropna().unique())
    list_of_index_1st_Sub_Ln = []
    for i in unique_1st_Sub_Ln:
        list_of_index_1st_Sub_Ln.extend(a.index[a['1st_Sub_Ln_Code']==i].tolist())
    total_person_1st_Sub_Ln = 0
    for i in list_of_index_1st_Sub_Ln:
        total_person_1st_Sub_Ln = total_person_1st_Sub_Ln + a['1st_Sub_Ln_Persons'][i]
    #total_person_1st_Sub_Ln.append(s2)
    
    # for second subsidiary langauge
    unique_2nd_Sub_Ln = list(a['2nd_Sub_Ln_Code'].dropna().unique())
    list_of_index_2nd_Sub_Ln = []
    for i in unique_2nd_Sub_Ln:
        list_of_index_2nd_Sub_Ln.extend(a.index[a['2nd_Sub_Ln_Code']==i].tolist())
    total_person_2nd_Sub_Ln = 0
    for i in list_of_index_2nd_Sub_Ln:
        total_person_2nd_Sub_Ln = total_person_2nd_Sub_Ln + a['2nd_Sub_Ln_Persons'][i]
    #total_person_2nd_Sub_Ln.append(s3)
    
    percent_one.append(((total_person_Main_Ln-total_person_1st_Sub_Ln)/total_person)*100)
    percent_two.append(((total_person_1st_Sub_Ln-total_person_2nd_Sub_Ln)/total_person)*100)
    percent_three.append((total_person_2nd_Sub_Ln/total_person)*100)
    


# In[15]:


# creating dataframe from lists, make the state code (numerical) in proper format, storing dataframe to csv
df1 = pd.DataFrame({'state-code':state_code,'percent-one':percent_one,'percent-two':percent_two,'percent-three':percent_three})
df1['state-code']=df1['state-code'].apply('="{}"'.format)
df1.to_csv('percent-india.csv',index=False)


# In[ ]:





# In[ ]:




