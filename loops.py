#!/usr/bin/env python
# coding: utf-8

# In[5]:


a='Bright IT career'
for i in range(1,11,1):
    print(a)


# In[9]:


i=1 
while i<=21:
    print(i)
    i=i+1


# In[15]:


i=int(input('enter num:'))
if i<101:
    if i%2==0:
        print('even num',i)
    else:
        print('odd num',i)


# In[1]:


## To print odd and even number among three numbers
for i in range(10,21,1):
    if i%2==0:
        print('even num',i)
    else:
        print('odd num',i)       


# In[2]:


### to print largest among three numbers
a=int(input('enter num:'))
b=int(input('enter num:'))
c=int(input('enter num:'))
if a>b:
    if a>c:
        print(a,"is the largest number")
    else:
         print(c,"is the largest number")
elif b>c:
     print(b,"is the largest number")
else:
     print(c,"is the largest number")


# In[6]:


i=int(input('enter num:'))
if i%2==0:
        print('even num',i)
else:
    print('odd num',i) 


# In[9]:


##to find armstrong number
a=int(input('enter num:'))
b=str(a)
c=0
while a>0:
    num=a%10
    c=c+num**len(b)
    a=a//10
print(c)


# In[10]:


##to find palindrome number
a=int(input('enter num:'))
b=str(a)
c=0
while a>0:
    num=a%10
    c=c*10+num
    a=a//10
print(c)


# In[11]:


##to find prime number
n=int(input('ntr num'))
for i in range(2,n):
    if n%i==0:
        print('n')
        break
else:
    print('s')   


# In[ ]:




