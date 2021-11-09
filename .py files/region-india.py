#!/usr/bin/env python
# coding: utf-8

# # Question-7

# In[1]:


# loading necessary libraries
import numpy as np
import pandas as pd


# In[2]:


North =['JAMMU & KASHMIR', 'PUNJAB', 'HIMACHAL PRADESH', 'HARYANA', 'UTTARAKHAND', 'NCT OF DELHI','CHANDIGARH']
West = [ 'RAJASTHAN', 'GUJARAT', 'MAHARASHTRA','GOA','DADRA & NAGAR HAVELI','DAMAN & DIU']
Central = ['MADHYA PRADESH', 'UTTAR PRADESH', 'CHHATTISGARH']
East = ['BIHAR', 'WEST BENGAL', 'ODISHA', 'JHARKHAND']
South = ['KARNATAKA', 'ANDHRA PRADESH', 'TAMIL NADU','KERALA','LAKSHADWEEP','PUDUCHERRY']
North_East = ['ASSAM', 'SIKKIM', 'MEGHALAYA', 'TRIPURA', 'ARUNACHAL PRADESH', 'MANIPUR', 'NAGALAND', 'MIZORAM','ANDAMAN & NICOBAR ISLANDS']


# In[3]:


# loading dataset to get Area_Names
data = pd.read_excel("DDW-C18-0000.XLSX",header=5)
# renaming columns and show the dataset
c = ['State_Code','District_Code','Area_Name','Total/Rural/Urban','Age_Group','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
data.columns = c
data


# In[4]:


# list of states, union terrotories along with "INDIA"
Area_Name=list(data['Area_Name'].unique())
Area_Name


# In[5]:


Area_Name.remove('INDIA')


# In[6]:


ind=[]
region_of_state=[]
j=[]
for i in range(35):
    if Area_Name[i] in North:
        region_of_state.append("North")
        ind.append(i)
    elif Area_Name[i] in West:
        region_of_state.append("West")
        ind.append(i)
    elif Area_Name[i] in Central:
        region_of_state.append("Central")
        ind.append(i)
    elif Area_Name[i] in East:
        region_of_state.append("East")
        ind.append(i)
    elif Area_Name[i] in South:
        region_of_state.append("South")
        ind.append(i)
    elif Area_Name[i] in North_East:
        region_of_state.append("North_East")
        ind.append(i)
    


# In[7]:


region_of_state


# In[8]:


population_Main_Ln_North = dict()
population_Main_Ln_West = dict()
population_Main_Ln_Central = dict()
population_Main_Ln_East = dict()
population_Main_Ln_South = dict()
population_Main_Ln_North_East = dict()

population_All_Ln_North = dict()
population_All_Ln_West = dict()
population_All_Ln_Central = dict()
population_All_Ln_East = dict()
population_All_Ln_South = dict()
population_All_Ln_North_East = dict()


mt_list_North_Main=[]
mt_list_West_Main=[]
mt_list_Central_Main=[]
mt_list_East_Main=[]
mt_list_South_Main=[]
mt_list_North_East_Main=[]

mt_list_North_All=[]
mt_list_West_All=[]
mt_list_Central_All=[]
mt_list_East_All=[]
mt_list_South_All=[]
mt_list_North_East_All=[]


# In[9]:


# for part(a)
# for first 9 datasets having "DDW-C17-0i00.XLSX" format, i is from 1 to 9
for j in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    
    if region_of_state[j-1]=='North':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_Main =list(set(l).union(set(mt_list_North_Main)))
        for i in mt_list_North_Main:
            if i in l:
                if i in population_Main_Ln_North:
                    population_Main_Ln_North[i] = population_Main_Ln_North[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_North[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_West_Main =list(set(l).union(set(mt_list_West_Main)))
        for i in mt_list_West_Main:
            if i in l:
                if i in population_Main_Ln_West:
                    population_Main_Ln_West[i] = population_Main_Ln_West[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_West[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_Central_Main =list(set(l).union(set(mt_list_Central_Main)))
        for i in mt_list_Central_Main:
            if i in l:
                if i in population_Main_Ln_Central:
                    population_Main_Ln_Central[i] = population_Main_Ln_Central[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_Central[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_East_Main =list(set(l).union(set(mt_list_East_Main)))
        for i in mt_list_East_Main:
            if i in l:
                if i in population_Main_Ln_East:
                    population_Main_Ln_East[i] = population_Main_Ln_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_South_Main =list(set(l).union(set(mt_list_South_Main)))
        for i in mt_list_South_Main:
            if i in l:
                if i in population_Main_Ln_South:
                    population_Main_Ln_South[i] = population_Main_Ln_South[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_South[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_East_Main =list(set(l).union(set(mt_list_North_East_Main)))
        for i in mt_list_North_East_Main:
            if i in l:
                if i in population_Main_Ln_North_East:
                    population_Main_Ln_North_East[i] = population_Main_Ln_North_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_North_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
     
    

    


# In[10]:


# for part(b)
## from main language
# for first 9 datasets having "DDW-C17-0i00.XLSX" format, i is from 1 to 9
for j in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
       
    
    if region_of_state[j-1]=='North':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_All =list(set(l).union(set(mt_list_North_All)))
        for i in mt_list_North_All:
            if i in l:
                if i in population_All_Ln_North:
                    population_All_Ln_North[i] = population_All_Ln_North[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_West_All =list(set(l).union(set(mt_list_West_All)))
        for i in mt_list_West_All:
            if i in l:
                if i in population_All_Ln_West:
                    population_All_Ln_West[i] = population_All_Ln_West[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_West[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_Central_All =list(set(l).union(set(mt_list_Central_All)))
        for i in mt_list_Central_All:
            if i in l:
                if i in population_All_Ln_Central:
                    population_All_Ln_Central[i] = population_All_Ln_Central[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_Central[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_East_All =list(set(l).union(set(mt_list_East_All)))
        for i in mt_list_East_All:
            if i in l:
                if i in population_All_Ln_East:
                    population_All_Ln_East[i] = population_All_Ln_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_South_All =list(set(l).union(set(mt_list_South_All)))
        for i in mt_list_South_All:
            if i in l:
                if i in population_All_Ln_South:
                    population_All_Ln_South[i] = population_All_Ln_South[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_South[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_East_All =list(set(l).union(set(mt_list_North_East_All)))
        for i in mt_list_North_East_All:
            if i in l:
                if i in population_All_Ln_North_East:
                    population_All_Ln_North_East[i] = population_All_Ln_North_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
     
    

    


# In[11]:


## from 1st_Sub language
# for first 9 datasets having "DDW-C17-0i00.XLSX" format, i is from 1 to 9
for j in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    
    
    if region_of_state[j-1]=='North':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_North_All =list(set(l).union(set(mt_list_North_All)))
        for i in mt_list_North_All:
            if i in l:
                if i in population_All_Ln_North:
                    population_All_Ln_North[i] = population_All_Ln_North[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_West_All =list(set(l).union(set(mt_list_West_All)))
        for i in mt_list_West_All:
            if i in l:
                if i in population_All_Ln_West:
                    population_All_Ln_West[i] = population_All_Ln_West[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_West[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_Central_All =list(set(l).union(set(mt_list_Central_All)))
        for i in mt_list_Central_All:
            if i in l:
                if i in population_All_Ln_Central:
                    population_All_Ln_Central[i] = population_All_Ln_Central[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_Central[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_East_All =list(set(l).union(set(mt_list_East_All)))
        for i in mt_list_East_All:
            if i in l:
                if i in population_All_Ln_East:
                    population_All_Ln_East[i] = population_All_Ln_East[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_East[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_South_All =list(set(l).union(set(mt_list_South_All)))
        for i in mt_list_South_All:
            if i in l:
                if i in population_All_Ln_South:
                    population_All_Ln_South[i] = population_All_Ln_South[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_South[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_North_East_All =list(set(l).union(set(mt_list_North_East_All)))
        for i in mt_list_North_East_All:
            if i in l:
                if i in population_All_Ln_North_East:
                    population_All_Ln_North_East[i] = population_All_Ln_North_East[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North_East[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
     


# In[12]:


## from 2nd_Sub language
# for first 9 datasets having "DDW-C17-0i00.XLSX" format, i is from 1 to 9
for j in range(1,10):
    a = pd.read_excel("DDW-C17-0"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    
    
    if region_of_state[j-1]=='North':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_North_All =list(set(l).union(set(mt_list_North_All)))
        for i in mt_list_North_All:
            if i in l:
                if i in population_All_Ln_North:
                    population_All_Ln_North[i] = population_All_Ln_North[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_West_All =list(set(l).union(set(mt_list_West_All)))
        for i in mt_list_West_All:
            if i in l:
                if i in population_All_Ln_West:
                    population_All_Ln_West[i] = population_All_Ln_West[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_West[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_Central_All =list(set(l).union(set(mt_list_Central_All)))
        for i in mt_list_Central_All:
            if i in l:
                if i in population_All_Ln_Central:
                    population_All_Ln_Central[i] = population_All_Ln_Central[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_Central[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_East_All =list(set(l).union(set(mt_list_East_All)))
        for i in mt_list_East_All:
            if i in l:
                if i in population_All_Ln_East:
                    population_All_Ln_East[i] = population_All_Ln_East[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_East[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_South_All =list(set(l).union(set(mt_list_South_All)))
        for i in mt_list_South_All:
            if i in l:
                if i in population_All_Ln_South:
                    population_All_Ln_South[i] = population_All_Ln_South[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_South[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_North_East_All =list(set(l).union(set(mt_list_North_East_All)))
        for i in mt_list_North_East_All:
            if i in l:
                if i in population_All_Ln_North_East:
                    population_All_Ln_North_East[i] = population_All_Ln_North_East[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North_East[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
     

    

    


# In[13]:


# for part(a)
# for remaining datasets having "DDW-C17-i00.XLSX" format, i is from 10 to 35  
for j in range(10,36):
    a = pd.read_excel("DDW-C17-"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    
    
    
    
    if region_of_state[j-1]=='North':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_Main =list(set(l).union(set(mt_list_North_Main)))
        for i in mt_list_North_Main:
            if i in l:
                if i in population_Main_Ln_North:
                    population_Main_Ln_North[i] = population_Main_Ln_North[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_North[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_West_Main =list(set(l).union(set(mt_list_West_Main)))
        for i in mt_list_West_Main:
            if i in l:
                if i in population_Main_Ln_West:
                    population_Main_Ln_West[i] = population_Main_Ln_West[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_West[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_Central_Main =list(set(l).union(set(mt_list_Central_Main)))
        for i in mt_list_Central_Main:
            if i in l:
                if i in population_Main_Ln_Central:
                    population_Main_Ln_Central[i] = population_Main_Ln_Central[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_Central[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_East_Main =list(set(l).union(set(mt_list_East_Main)))
        for i in mt_list_East_Main:
            if i in l:
                if i in population_Main_Ln_East:
                    population_Main_Ln_East[i] = population_Main_Ln_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_South_Main =list(set(l).union(set(mt_list_South_Main)))
        for i in mt_list_South_Main:
            if i in l:
                if i in population_Main_Ln_South:
                    population_Main_Ln_South[i] = population_Main_Ln_South[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_South[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_East_Main =list(set(l).union(set(mt_list_North_East_Main)))
        for i in mt_list_North_East_Main:
            if i in l:
                if i in population_Main_Ln_North_East:
                    population_Main_Ln_North_East[i] = population_Main_Ln_North_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_Main_Ln_North_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
     
    


# In[14]:


# for part(b)
## for main language
# for remaining datasets having "DDW-C17-i00.XLSX" format, i is from 10 to 35  
for j in range(10,36):
    a = pd.read_excel("DDW-C17-"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    

    
    if region_of_state[j-1]=='North':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_All =list(set(l).union(set(mt_list_North_All)))
        for i in mt_list_North_All:
            if i in l:
                if i in population_All_Ln_North:
                    population_All_Ln_North[i] = population_All_Ln_North[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_West_All =list(set(l).union(set(mt_list_West_All)))
        for i in mt_list_West_All:
            if i in l:
                if i in population_All_Ln_West:
                    population_All_Ln_West[i] = population_All_Ln_West[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_West[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_Central_All =list(set(l).union(set(mt_list_Central_All)))
        for i in mt_list_Central_All:
            if i in l:
                if i in population_All_Ln_Central:
                    population_All_Ln_Central[i] = population_All_Ln_Central[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_Central[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_East_All =list(set(l).union(set(mt_list_East_All)))
        for i in mt_list_East_All:
            if i in l:
                if i in population_All_Ln_East:
                    population_All_Ln_East[i] = population_All_Ln_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_South_All =list(set(l).union(set(mt_list_South_All)))
        for i in mt_list_South_All:
            if i in l:
                if i in population_All_Ln_South:
                    population_All_Ln_South[i] = population_All_Ln_South[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_South[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['Main_Ln_Name'].dropna().unique())
        mt_list_North_East_All =list(set(l).union(set(mt_list_North_East_All)))
        for i in mt_list_North_East_All:
            if i in l:
                if i in population_All_Ln_North_East:
                    population_All_Ln_North_East[i] = population_All_Ln_North_East[i] + a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North_East[i] = a['Main_Ln_Persons'][a.index[a['Main_Ln_Name']==i][0]]
     
 


# In[15]:


## for 1st_Sub language
# for remaining datasets having "DDW-C17-i00.XLSX" format, i is from 10 to 35  
for j in range(10,36):
    a = pd.read_excel("DDW-C17-"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
    
    
    if region_of_state[j-1]=='North':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_North_All =list(set(l).union(set(mt_list_North_All)))
        for i in mt_list_North_All:
            if i in l:
                if i in population_All_Ln_North:
                    population_All_Ln_North[i] = population_All_Ln_North[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_West_All =list(set(l).union(set(mt_list_West_All)))
        for i in mt_list_West_All:
            if i in l:
                if i in population_All_Ln_West:
                    population_All_Ln_West[i] = population_All_Ln_West[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_West[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_Central_All =list(set(l).union(set(mt_list_Central_All)))
        for i in mt_list_Central_All:
            if i in l:
                if i in population_All_Ln_Central:
                    population_All_Ln_Central[i] = population_All_Ln_Central[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_Central[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_East_All =list(set(l).union(set(mt_list_East_All)))
        for i in mt_list_East_All:
            if i in l:
                if i in population_All_Ln_East:
                    population_All_Ln_East[i] = population_All_Ln_East[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_East[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_South_All =list(set(l).union(set(mt_list_South_All)))
        for i in mt_list_South_All:
            if i in l:
                if i in population_All_Ln_South:
                    population_All_Ln_South[i] = population_All_Ln_South[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_South[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['1st_Sub_Ln_Name'].dropna().unique())
        mt_list_North_East_All =list(set(l).union(set(mt_list_North_East_All)))
        for i in mt_list_North_East_All:
            if i in l:
                if i in population_All_Ln_North_East:
                    population_All_Ln_North_East[i] = population_All_Ln_North_East[i] + a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North_East[i] = a['1st_Sub_Ln_Persons'][a.index[a['1st_Sub_Ln_Name']==i][0]]
     


# In[16]:


## for 2nd_Sub language
# for remaining datasets having "DDW-C17-i00.XLSX" format, i is from 10 to 35  
for j in range(10,36):
    a = pd.read_excel("DDW-C17-"+str(j)+"00.XLSX",header=5)
    
    c = ['State_Code','Area_Name','Main_Ln_Code','Main_Ln_Name','Main_Ln_Persons','Main_Ln_Males','Main_Ln_Females','1st_Sub_Ln_Code','1st_Sub_Ln_Name','1st_Sub_Ln_Persons','1st_Sub_Ln_Males','1st_Sub_Ln_Females','2nd_Sub_Ln_Code','2nd_Sub_Ln_Name','2nd_Sub_Ln_Persons','2nd_Sub_Ln_Males','2nd_Sub_Ln_Females']
    a.columns = c
    
   
    if region_of_state[j-1]=='North':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_North_All =list(set(l).union(set(mt_list_North_All)))
        for i in mt_list_North_All:
            if i in l:
                if i in population_All_Ln_North:
                    population_All_Ln_North[i] = population_All_Ln_North[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
        
    elif region_of_state[j-1]=='West':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_West_All =list(set(l).union(set(mt_list_West_All)))
        for i in mt_list_West_All:
            if i in l:
                if i in population_All_Ln_West:
                    population_All_Ln_West[i] = population_All_Ln_West[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_West[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]] 
        
    elif region_of_state[j-1]=='Central':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_Central_All =list(set(l).union(set(mt_list_Central_All)))
        for i in mt_list_Central_All:
            if i in l:
                if i in population_All_Ln_Central:
                    population_All_Ln_Central[i] = population_All_Ln_Central[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_Central[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='East':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_East_All =list(set(l).union(set(mt_list_East_All)))
        for i in mt_list_East_All:
            if i in l:
                if i in population_All_Ln_East:
                    population_All_Ln_East[i] = population_All_Ln_East[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_East[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='South':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_South_All =list(set(l).union(set(mt_list_South_All)))
        for i in mt_list_South_All:
            if i in l:
                if i in population_All_Ln_South:
                    population_All_Ln_South[i] = population_All_Ln_South[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_South[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                
    elif region_of_state[j-1]=='North_East':
        l = list(a['2nd_Sub_Ln_Name'].dropna().unique())
        mt_list_North_East_All =list(set(l).union(set(mt_list_North_East_All)))
        for i in mt_list_North_East_All:
            if i in l:
                if i in population_All_Ln_North_East:
                    population_All_Ln_North_East[i] = population_All_Ln_North_East[i] + a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
                else:
                    population_All_Ln_North_East[i] = a['2nd_Sub_Ln_Persons'][a.index[a['2nd_Sub_Ln_Name']==i][0]]
     


# In[17]:


# for part(a)

language_1_one = []
language_2_one = []
language_3_one = []

#population_Main_Ln_North
v=list(population_Main_Ln_North.values())
k=list(population_Main_Ln_North.keys())

t=v.index(max(v))
language_1_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_one.append(k[t])
            

#population_Main_Ln_West
v=list(population_Main_Ln_West.values())
k=list(population_Main_Ln_West.keys())

t=v.index(max(v))
language_1_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_one.append(k[t])


#population_Main_Ln_Central
v=list(population_Main_Ln_Central.values())
k=list(population_Main_Ln_Central.keys())

t=v.index(max(v))
language_1_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_one.append(k[t])


#population_Main_Ln_East
v=list(population_Main_Ln_East.values())
k=list(population_Main_Ln_East.keys())

t=v.index(max(v))
language_1_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_one.append(k[t])


#population_Main_Ln_South
v=list(population_Main_Ln_South.values())
k=list(population_Main_Ln_South.keys())

t=v.index(max(v))
language_1_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_one.append(k[t])


#population_Main_Ln_NorthEast
v=list(population_Main_Ln_North_East.values())
k=list(population_Main_Ln_North_East.keys())

t=v.index(max(v))
language_1_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_one.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_one.append(k[t])


# In[18]:


region=['North','West','Central', 'East','South','North_East']


# In[19]:


d1 = pd.DataFrame(list(zip(region,language_1_one,language_2_one,language_3_one)),columns=['region', 'language-1', 'language-2', 'language-3'])
d1


# In[20]:


d1.to_csv('region-india-{a}.csv')


# In[21]:


# for part(b)

language_1_all = []
language_2_all = []
language_3_all = []

#population_All_Ln_North
v=list(population_All_Ln_North.values())
k=list(population_All_Ln_North.keys())

t=v.index(max(v))
language_1_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_all.append(k[t])
            

#population_All_Ln_West
v=list(population_All_Ln_West.values())
k=list(population_All_Ln_West.keys())

t=v.index(max(v))
language_1_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_all.append(k[t])


#population_All_Ln_Central
v=list(population_All_Ln_Central.values())
k=list(population_All_Ln_Central.keys())

t=v.index(max(v))
language_1_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_all.append(k[t])


#population_All_Ln_East
v=list(population_All_Ln_East.values())
k=list(population_All_Ln_East.keys())

t=v.index(max(v))
language_1_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_all.append(k[t])


#population_All_Ln_South
v=list(population_All_Ln_South.values())
k=list(population_All_Ln_South.keys())

t=v.index(max(v))
language_1_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_all.append(k[t])


#population_All_Ln_NorthEast
v=list(population_All_Ln_North_East.values())
k=list(population_All_Ln_North_East.keys())

t=v.index(max(v))
language_1_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_2_all.append(k[t])
v.pop(t)
k.pop(t)

t=v.index(max(v))
language_3_all.append(k[t])


# In[22]:


d2 = pd.DataFrame(list(zip(region,language_1_all,language_2_all,language_3_all)),columns=['region', 'language-1', 'language-2', 'language-3'])
d2


# In[23]:


d2.to_csv('region-india-{b}.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




