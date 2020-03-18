#!/usr/bin/env python
# coding: utf-8

# <<<<<--------------OOPS--------------->>>>>>>>>>>>>

# <<<<<<<<<<<--------------Class and Object------------------------>>>>>>>>>>>>>>

# In[53]:


class computer:
    def details(self):
        print("2Gib,16vCPU,1tb Hard Drive")
        #spec=computer()
        #computer.details(spec)
        #faced RecursionError
        
spec=computer()     
mod=computer() #defined here about which class is belongs to.
computer.details(spec)  #we are defining the class and methods(function) itself here.
computer.details(mod)    #"details" func atleast need 1 parameter to pass self. 
print(type(spec))
spec=computer()   #storing class in the object, to indicate that which class is belongs too.
spec.details()


# In[43]:


#if we are looking pre-defined types
x=10

print(type(x))   #class type is "int", it's a in built-class type.

print(type(mod)) #computer is our defined class type.


# In[ ]:




