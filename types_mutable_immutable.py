#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy

x = 100
y = copy.copy(x+1)
print(id(x))
print(id(y))
y+=10
print(id(x))
print(id(y))


# In[2]:


try: print(x)
except:pass


# In[8]:



try:
    number = int(input('enter a number: '))
    raise Exception('smth went wrong!!234567')
    res = 100 / number
    print(res)
except ZeroDivisionError as e:
    print('cant divide by zero - error')
    print(e)

else:
    print('no errors')
finally:
    print('do smth finally')


# In[ ]:





# In[ ]:




