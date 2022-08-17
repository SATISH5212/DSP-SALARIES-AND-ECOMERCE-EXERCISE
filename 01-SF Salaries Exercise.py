#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[18]:


sal=pd.read_csv("salaries.csv")
pd.DataFrame(sal)


# ** Check the head of the DataFrame. **

# In[19]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[20]:


sal.info()


# In[ ]:





# In[9]:





# **What is the average BasePay ?**

# In[21]:


sal["BasePay"].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[22]:


sal["OvertimePay"].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[27]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[28]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[38]:


sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].max()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[39]:


sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].min()]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[42]:


sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[44]:


sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[45]:


groups= sal.groupby('JobTitle').count()
top5= groups.sort_values(by='Id',  ascending=False)[:5]
top5['Id']


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[46]:


copied_sal = sal[sal['Year'] == 2013]
group = copied_sal.groupby('JobTitle').count()
count = group[group['Id'] == 1]
count.count()['Id']


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[48]:


def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

sal = pd.read_csv('Salaries.csv')



# In[49]:


sum(sal['JobTitle'].apply(lambda x: find_chief(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[57]:


sal['title_len'] = sal['JobTitle'].apply(len)

sal[['title_len', 'TotalPayBenefits']].corr()


# In[23]:





# # Great Job!
