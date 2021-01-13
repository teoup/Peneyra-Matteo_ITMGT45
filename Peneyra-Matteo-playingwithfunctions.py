#!/usr/bin/env python
# coding: utf-8

# ## 1 
# ### 1 point
# #### Write a function that takes the circumference of a circle as a parameter and returns the area of that circle.
# #### Note: Assume the value of pi is 3.1416

# In[14]:


def area_of_circle(area):
    radius = n / 6.2832
    area = ((radius ** 2) * 3.1416)
    return area

n = 11
              
print("The area of the circle is", area_of_circle(n))


# ## 2
# ### 2 points
# #### Write a function that takes a 5-character string as a parameter and returns the string in reverse order. 
# #### e.g. reverseString("Hello") -> "olleH"

# In[17]:


def reverse(string):
    string = "".join(reversed(string))
    return string

s = ("Happy")

print ("reverseString",(s) , "->" , end =  "") 
print (reverse(s)) 


# ## 3
# ### 2 points
# #### Write a function that takes a positive integer as input and returns the sum of all positive integers smaller than and including the number itself.
# #### e.g. backAddition(5) -> 1 + 2 + 3 + 4 + 5 -> 15

# In[16]:


n = float(input("Positive integer: "))

def sum_int(result):
    result = (n * (n + 1)) / 2
    return result

print("backAddition", n, "->",sum_int(n))


# ## 4
# ### 5 points (all or nothing)
# #### Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# In[10]:


def diff_numbers(result):
    sumofsquares = (n * (n+1) * (2 * n + 1)) /6
    squareofsum = sum(r) ** 2
    result = squareofsum - sumofsquares
    return result

r = (1, 101)

print(diff_numbers(r))


# In[ ]:




