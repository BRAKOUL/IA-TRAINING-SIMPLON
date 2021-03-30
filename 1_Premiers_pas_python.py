#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1
print(a)


# In[4]:


# Les types de variables
a = 1
print(type(a))
b = 1.0
print(type(b))
c = 'bonjour'
print(type(c))


# In[7]:


# operation entre type différents
a = 9
b = a/2
print(b)
print(type(b))
b = a//2
print(b)
print(type(b))


# In[8]:


# convertir un type en un autre - str to int
a = '123'
b = int(a)
print(b+1)
print(type(b))


# In[9]:


# convertir un type en un autre - str to float
a = '123.5'
b = float(a)
print(b+1)
print(type(b))


# In[12]:


# Convertir un type en un autre - float to int
a = 123.5
b = int(a)
print(type(b))
print(b)


# In[13]:


# Convertir un type en un autre - int/float to str
a = 7
b = 3.14

c = str(a)
d = str(b)

print(type(c))
print(type(d))
print(c,d)


# In[19]:


# Determiner la valeur retournée, True ou False, par chaque expression conditionnelle:
A = B = True
C = D = False
print((A or B) and (C or D))
print(A or (B and C))
print (A and B and (C or D))
print((A and B) or (not C))
print((not A) or D)


# In[25]:


# Donnez les valeurs retournées par chacune des expressions suivantes
print( abs(-3) + max(3,4))
print( min(4,8,0,-2))
print(max(min(7,8), min(4,6)))
print(round(8.324) + round(8.88))
print(round(8.98795136,3))


# In[43]:


from math import sqrt
a = 3
b = -7
c = -23
delta = b**2 - 4*a*c
print(delta)
X1 = (-b - (sqrt(delta)))/(2*a)
X2 = (-b + (sqrt(delta)))/(2*a)
print(X1, X2)


# In[47]:


from math import *
r = int(input())
h = int(input())
v = (pi/3)*(r**2)*h
print(v)


# In[ ]:




