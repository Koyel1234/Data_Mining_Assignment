#!/usr/bin/env python
# coding: utf-8

# # Question-6

# In[1]:


# loading necessary libraries
import numpy as np
import pandas as pd


# In[2]:


# loading dataset for education-level-wise computation
data = pd.read_excel("DDW-C19-0000.XLSX",header=5)


# In[3]:


# renaming columns and show the dataset
c = ['State_Code','District_Code','Area_Name','Total/Rural/Urban','Educational_Level','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
data.columns = c
data


# In[4]:


# excel file hassome extra rows at the end, so removing them 
data=data.iloc[0:864,]


# In[5]:


# list of states, union terrotories along with "INDIA"
Area_List=list(data['Area_Name'].unique())
Area_List


# In[6]:


# list of different educational levels
Educational_List=list(data['Educational_Level'].unique())
Educational_List


# In[7]:


# remove 'Total' from list
Educational_List.remove('Total')


# In[8]:


Area_Name = []
total_population =[]


# In[9]:


# load dataset to calculate totalpopulation of India
data_INDIA =pd.read_excel("DDW-C17-0000.XLSX",header=5)

c = ['State_Code','State_Name','Main_Ln_Code','main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
data_INDIA.columns = c
data_INDIA


# calculation total population in India, as each will have one unique mother toungue, sum of all people from mother toungue will produce total population in India
l=list(data_INDIA['Main_Ln_Code'].dropna().unique())
list_of_index = []
for i in l:
    list_of_index.extend(data_INDIA.index[data_INDIA['Main_Ln_Code']==i].tolist())
total_person = 0
for i in list_of_index:
    total_person = total_person + data_INDIA['Main_Ln_Persons'][i]
total_person

Area_Name.append('INDIA')
total_population.append(total_person)


# In[10]:


# for first 9 datasets having "DDW-C17-0i00.XLSX" format, i is from 1 to 9
for i in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(i)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    # for state/ut name
    y = list(a['Area_Name'].dropna().unique())
    Area_Name.extend(y)
    
    unique_Main_Ln = list(a['Main_Ln_Code'].dropna().unique())
    list_of_index_Main_Ln = []
    for i in unique_Main_Ln:
        list_of_index_Main_Ln.extend(a.index[a['Main_Ln_Code']==i].tolist())
    total_person_Main_Ln = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln = total_person_Main_Ln + a['Main_Ln_Persons'][i]
    
    
    total_population.append(total_person_Main_Ln)
    
    

# for remaining datasets having "DDW-C17-i00.XLSX" format, i is from 10 to 35   
for i in range(10,36):
    a = pd.read_excel("DDW-C17-"+str(i)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    # for state/ut name
    y = list(a['Area_Name'].dropna().unique())
    Area_Name.extend(y)
    
    
    # for main language
    unique_Main_Ln = list(a['Main_Ln_Code'].dropna().unique())
    list_of_index_Main_Ln = []
    for i in unique_Main_Ln:
        list_of_index_Main_Ln.extend(a.index[a['Main_Ln_Code']==i].tolist())
    total_person_Main_Ln = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln = total_person_Main_Ln + a['Main_Ln_Persons'][i]
    
    
    
    total_population.append(total_person_Main_Ln)


# In[11]:


# make dataframe from Area_Name and total_population
df = pd.DataFrame(list(zip(Area_Name,total_population)),columns=['Area_Name','total_population'])
df


# In[12]:


# calculate age for maximum percentage for three or more languages in each state
state_ut=[]
literacy_group=[]
percentage=[]
for i in Area_List:
    state_ut.append(i)
    p=[]
    for j in Educational_List:
        d1=data.loc[(data['Area_Name']==i) & (data['Educational_Level']==j)].reset_index(drop=True)
        d2=d1[['Area_Name','2nd_Sub_Ln_Persons']]
        d3=df[df['Area_Name']==i].reset_index(drop=True)
        #age_group.append(j)
        p.append((d2['2nd_Sub_Ln_Persons'][0]/d3['total_population'][0])*100)
    literacy_group.append(Educational_List[p.index(max(p))])
    percentage.append(max(p))


# In[13]:


# resulting dataframe
result = pd.DataFrame(list(zip(state_ut,literacy_group,percentage)),columns=['state/ut','literacy_group','percentage'])
result


# In[14]:


# exporting to csv
result.to_csv('literacy-india.csv')


# In[ ]:





# In[ ]:





# In[ ]:




