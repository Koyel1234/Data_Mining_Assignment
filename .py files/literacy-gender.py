#!/usr/bin/env python
# coding: utf-8

# # Question - 9

# In[1]:


# loading necessary libraries
import numpy as np
import pandas as pd


# In[2]:


# loading dataset for education level wise computation
data = pd.read_excel("DDW-C19-0000.XLSX",header=5)


# In[3]:


# renaming columns and show the dataset
c = ['State_Code','District_Code','Area_Name','Total/Rural/Urban','Educational_Level','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
data.columns = c
data


# In[19]:


# excel file hassome extra rows at the end, so removing them 
data=data.iloc[0:864,]


# In[20]:


# list of states, union terrotories along with "INDIA"
Area_List=list(data['Area_Name'].unique())
Area_List


# In[5]:


len(Area_List)


# In[21]:


# list of different age groups
Educational_Level_List=list(data['Educational_Level'].unique())
Educational_Level_List


# In[7]:


# remove 'Total' from list
Educational_Level_List.remove('Total')


# In[24]:


Area_Name = []
total_population_males =[]
total_population_females =[]


# In[25]:


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
total_person_males = 0
total_person_females = 0
for i in list_of_index:
    total_person_males = total_person_males + data_INDIA['Main_Ln_Males'][i]
    total_person_females = total_person_females + data_INDIA['Main_Ln_Females'][i]


Area_Name.append('INDIA')
total_population_males.append(total_person_males)
total_population_females.append(total_person_females)


# In[26]:


# for first 9 datasets having "DDW-C17-0i00.XLSX" format, i is from 1 to 9
for i in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(i)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    # for state/ut name
    y = list(a['Area_Name'].dropna().unique())
    Area_Name.extend(y)
    
    unique_Main_Ln = list(a['Main_Ln_Code'].dropna().unique())
    list_of_index_Main_Ln = []
    for i in unique_Main_Ln:
        list_of_index_Main_Ln.extend(a.index[a['Main_Ln_Code']==i].tolist())
    total_person_Main_Ln_males = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln_males = total_person_Main_Ln_males + a['Main_Ln_Males'][i]
    total_person_Main_Ln_females = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln_females = total_person_Main_Ln_females + a['Main_Ln_Females'][i]
    
    
    total_population_males.append(total_person_Main_Ln_males)
    total_population_females.append(total_person_Main_Ln_females)
    
    
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
    total_person_Main_Ln_males = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln_males = total_person_Main_Ln_males + a['Main_Ln_Males'][i]
    total_person_Main_Ln_females = 0
    for i in list_of_index_Main_Ln:
        total_person_Main_Ln_females = total_person_Main_Ln_females + a['Main_Ln_Females'][i]
    
    
    
    total_population_males.append(total_person_Main_Ln_males)
    total_population_females.append(total_person_Main_Ln_females)


# In[27]:


# make dataframe from Area_Name and total_population
df = pd.DataFrame(list(zip(Area_Name,total_population_males,total_population_females)),columns=['Area_Name','total_population_males','total_population_females'])
df


# In[28]:


# calculate age for maximum ratio for three or more languages in each state
state_ut=[]
educational_level_males_a=[]
educational_level_females_a=[]
educational_level_males_b=[]
educational_level_females_b=[]
ratio_males_a=[]
ratio_females_a=[]
ratio_males_b=[]
ratio_females_b=[]

for i in Area_List:
    state_ut.append(i)
    p_males_a=[]
    p_females_a=[]
    p_males_b=[]
    p_females_b=[]
    for j in Educational_Level_List:
        d1=data.loc[(data['Area_Name']==i) & (data['Educational_Level']==j)].reset_index(drop=True)
        d2=d1[['Area_Name','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']]
        d3=df[df['Area_Name']==i].reset_index(drop=True)
        
        p_males_a.append(d2['2nd_Sub_Ln_Males'][0]/d3['total_population_males'][0])
        p_females_a.append(d2['2nd_Sub_Ln_Females'][0]/d3['total_population_females'][0])
        p_males_b.append((d2['1st_Sub_Ln_Males'][0]-d2['2nd_Sub_Ln_Males'][0])/d3['total_population_males'][0])
        p_females_b.append((d2['1st_Sub_Ln_Females'][0]-d2['2nd_Sub_Ln_Females'][0])/d3['total_population_females'][0])
        
        
    educational_level_males_a.append(Educational_Level_List[p_males_a.index(max(p_males_a))])
    educational_level_females_a.append(Educational_Level_List[p_females_a.index(max(p_females_a))])
    educational_level_males_b.append(Educational_Level_List[p_males_b.index(max(p_males_b))])
    educational_level_females_b.append(Educational_Level_List[p_females_b.index(max(p_females_b))])
    ratio_males_a.append(max(p_males_a))
    ratio_females_a.append(max(p_females_a))
    ratio_males_b.append(max(p_males_b))
    ratio_females_b.append(max(p_females_b))


# In[29]:


# resulting dataframe for part(a)
result_a = pd.DataFrame(list(zip(state_ut,educational_level_males_a,ratio_males_a,educational_level_females_a,ratio_females_a)),columns=['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females'])
result_a


# In[30]:


# exporting to csv far part(a)
result_a.to_csv('literacy-gender-{a}.csv')


# In[31]:


# resulting dataframe for part(a)
result_b = pd.DataFrame(list(zip(state_ut,educational_level_males_b,ratio_males_b,educational_level_females_b,ratio_females_b)),columns=['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females'])
result_b


# In[32]:


# exporting to csv far part(b)
result_b.to_csv('literacy-gender-{b}.csv')


# In[ ]:





# In[ ]:




