#!/usr/bin/env python
# coding: utf-8

# # Bubble Sort Algorithm
# 
# ### Time Complexity:O($ n^2 $)
# ### Space Complexity:O(1)

# In[2]:


def Bubble_Sort(nums):
    for i in  range(len(nums)):
        for j in range(1,len(nums)):
            prev=nums[j-1]
            cur=nums[j]
            
            if prev<=cur:
                continue
                
            nums[j-1]=cur
            nums[j]=prev
    return nums

print(Bubble_Sort([9,4,67,78,24,14,0]))

