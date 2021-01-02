#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


print(np.__version__)


# In[3]:


arr = np.arange(10)


# In[4]:


arr


# In[5]:


np.full((3, 3), True, dtype=bool)


# In[6]:


np.ones((3,3), dtype=bool)


# In[7]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[8]:


arr[arr % 2 == 1]


# In[9]:


arr[arr % 2 == 1] = -1


# In[10]:


arr


# In[11]:


arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
out


# In[12]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])


# In[13]:


np.intersect1d(a,b)


# In[14]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])


# In[15]:


np.setdiff1d(a,b)


# In[16]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])


# In[17]:


np.where(a == b)


# In[18]:


a = np.array([2, 6, 1, 9, 10, 3, 27])


# In[19]:


a = np.arange(15)


# In[20]:


index = np.where((a >= 5) & (a <= 10))
a[index]


# In[21]:


def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

maxx(1, 5)


# In[23]:


def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max(a, b)


# In[24]:


arr = np.arange(9).reshape(3,3)
arr


# In[25]:


arr = np.arange(9).reshape(3,3)


# In[26]:


arr[[1,0,2], :]


# In[27]:


arr[::-1]


# In[28]:


arr[:, ::-1]


# In[29]:


rand_arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))


# In[30]:


rand_arr = np.random.uniform(5,10, size=(5,3))
print(rand_arr)


# In[31]:


rand_arr = np.random.random((5,3))


# In[32]:


np.set_printoptions(precision=3)
rand_arr[:4]


# In[33]:


np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
rand_arr


# In[34]:


np.set_printoptions(suppress=False)


# In[35]:


np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
rand_arr


# In[ ]:




