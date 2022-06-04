#!/usr/bin/env python
# coding: utf-8

# In[36]:


ice_cream_rating = 10
sleeping_rating = 10


# In[37]:


print('Enter your first name')
first_name = input()


# In[38]:


print('Enter your last name')
last_name = input()


# In[39]:


my_name = first_name  + ' ' + last_name


# In[40]:


print(my_name)


# In[56]:


import math
happiness_rating = ((ice_cream_rating + sleeping_rating) / 2)


# In[50]:


print(type(ice_cream_rating))
print(type(first_name))
print(type(happiness_rating))


# In[22]:


# The happiness_rating type surprised me.  I thought it would return an integer type but instead it was converted to a float


# In[70]:


happiness_percentage = (happiness_rating) / ((ice_cream_rating + sleeping_rating) /2)

print('My name is', first_name, 'and I give eating ice cream a score of' , ice_cream_rating , 'out of 10!')
print('I am', my_name, 'and my sleeping enjoyment rating is', sleeping_rating, '/ 10')
print('Based on the factors above, my happiness rating is', happiness_rating, 'out of 10', 'or', format(happiness_percentage,'.2%'))


# In[ ]:




