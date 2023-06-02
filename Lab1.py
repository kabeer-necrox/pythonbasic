#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:





# In[3]:





# In[5]:





# In[6]:


print("hello kabir")


# In[14]:


def print_triangle(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()

# Example usage:
print_triangle(5)






# In[1]:


print(1 + 1)


# In[ ]:


print(2 + 4)


# In[ ]:


print(6)


# In[1]:


print("hello everyone")


# In[1]:


print(" *")
print("   **")
print("    ****")


# In[8]:


print("hhhhhh")
print("hhhh")
print("hhh")
print("hh")
print("h")


# In[9]:


3/2*3


# In[10]:


-23%7


# In[11]:


bool(0)


# In[12]:


bool(5)


# In[13]:


float(10)


# In[18]:


radius = 5
pi = 3.14
area = pi**2*radius
print(area)


# In[19]:


radius = 5
pi = 3.14
circumference = 2*pi*radius**2
print(circumference)


# In[23]:


str1 = "M. Ali, Abdullah, Ali"
print(str1.split(", "))


# In[31]:


num1, num2 =input("enter ist number").split()
num1, num2 = int(num1), int(num2)

print("the sum of two number is ", num1 + num2)
print("the product of two number", num1 * num2)
print("the quotient of two number", num1 / num2)
print("the reminder of the two number", num1 % num2)


# In[32]:


54 > 30


# In[33]:


30 < 20


# In[34]:


43 != 30


# In[2]:


import random
num_to_guess = random.randint(1,100)

num_to_guess


# In[ ]:


num = random.randint(1,100)
while True:
    gussed_num = int(input("guess a number between 1 and 100"))
    if gussed_num==num:
        print("conguratulation you gurrd correct")
        break
    if gussed_num>num:
        print("higher then guess number")
    if gussed_num<num:
        print("smiller then guess number")
            


# In[1]:


False and False or True 


# In[2]:


user1 = "Ali"
user2 = "Noman"
user = ""


# In[3]:


if user1:
    print("new_uer")
    if user2


# In[4]:


list1 = ["ali", "Noman","Abdullah"]


# In[5]:


list1.append("Ahsan")


# In[6]:


list1


# In[8]:


list1[2]


# In[9]:


list1[-2]


# In[10]:


list1[1:3]


# In[11]:


list1[::]


# In[12]:


list1[0::3]


# In[13]:


list1[1::2]


# In[14]:


list1[::-1]


# In[15]:


list1[::1]


# In[16]:


list1[0:5:3]


# In[18]:


list1.pop(1)


# In[19]:


list1.pop(2)


# In[20]:


list1.pop(-2)


# In[22]:


list1.append("kabeer")


# In[26]:


list1[:]


# In[27]:


list1


# In[28]:





# In[30]:


list1


# In[35]:


print(list1)


# In[37]:


list1.extend(["saleem","azhar","shair"])


# In[38]:


list1


# In[45]:


for i in range(20):
  print(i)


# In[46]:


i = 10
while  i > 5:
    print(i)
    i = i-1


# In[51]:


age_of_students = [22, 21, 32, 33, 44, 34]


# In[55]:


new_age = []
for i in age_of_students:
    new_age.append(i-3)
    print(new_age)


# In[2]:


no_of_vals =int(input("enter the number of values into input"))


# In[ ]:


list_of_nums = []
for i in range(no_of_vals):
    last_num = int(input("enter val no." + str(i+1) + ":"))
    if i == 0:
        min_val = last_num
    else:
        min_val = min(min_val, last_num)
    print(min_val)
        


# In[7]:


i = 1 
result = 0
while i <= 5:
    a = input("enter five number")
    result = result + int(a)
    i = i +1
print("sum of the five number:", result)


# In[15]:


name = "kabeer"

for _ in range(10):
    print(name)


# In[18]:


name = "shair"
for _ in range(5):
    print(name)


# In[1]:


pow(2,4)


# In[2]:


pow(2,4,8)


# In[3]:


round(3.8)


# In[4]:


round(3.3)


# In[5]:


round(3.5)


# In[6]:


round(-3.5)


# In[7]:


round(98.5)


# In[14]:


def mynNm(){
    print("kabeer is here")
}
mynam()


# In[ ]:




