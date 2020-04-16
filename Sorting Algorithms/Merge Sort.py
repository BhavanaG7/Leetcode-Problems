#!/usr/bin/env python
# coding: utf-8

# # Merge Sort
# 
# ### Time Complexity:O(nlogn)
# ### Space Complexity:O(n)

# In[1]:


def merge_sort(nums):
    if len(nums)<=1:
        return nums
    
    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]
    
    left=merge_sort(left)
    right=merge_sort(right)
    
    return merge(left,right)

def merge(left,right):
    left_index=0
    right_index=0
    merged=[]
    
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1
            
    merged+=left[left_index:]
    merged+=right[right_index:]
    
    return merged


# In[ ]:


nums=list(map(int,input().rstrip().split()))
print(merge_sort(nums))


# In[ ]:




