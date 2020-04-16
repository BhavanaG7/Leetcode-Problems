#!/usr/bin/env python
# coding: utf-8

# # Max Heap
# 

# In[18]:


class MaxHeap:
    def __init__(self,items=[]):
        super().__init__()

        #create heap list having 0th index value as 0
        self.heap_list=[0]

        for i in items:
            self.heap_list.append(i)
            self.__floatup(len(self.heap_list)-1)

    #to add element to the heap
    def push(self,value):
        #append the value to the heap and then float up the value
        #floatup(index_value)
        self.heap_list.append(value)
        self.__floatup(len(self.heap_list)-1)

    #to get the max element i.e,the root element
    def peek(self):
        if self.heap_list[1] is not None:
            return self.heap_list[1]
        else:
            return False

    def pop(self):
        #trying to pop from empty list , 1 because initial heap contains [0]
        if len(self.heap_list)<=1:
            return False

        #if heap contains only 1 element along with initial [0] i.e, [0,1] or [0,2]
        #pop it and assign it to variable max . since when we pop we always pop the maximum element
        elif len(self.heap_list)==2:
            max=self.heap_list.pop()

        #when the length is greater than 2
        #1.we swap the last and and the first root element
        #2.pop 
        #3.bubbledown the heap. i.e, rearrange the heap
        else:
            self.__swap(1,len(self.heap_list)-1)
            max=self.heap_list.pop()
            self.__bubbledown(1)

        return max

    #swap(index1,index2)
    def __swap(self,a,b):
        self.heap_list[a],self.heap_list[b]=self.heap_list[b],self.heap_list[a]
            
    def __floatup(self,index):
        #if index is 1 no floatup is required since it is the first element
        if index<=1:
            return
        else:
            parent=index//2

            if self.heap_list[parent]<self.heap_list[index]:
                self.__swap(index,parent)
                self.__floatup(parent)

    #heapify function
    def __bubbledown(self,index):
        left=index*2
        right=index*2+1

        largest=index

        if left<len(self.heap_list) and self.heap_list[largest]<self.heap_list[left]:
            largest=left

        if right<len(self.heap_list) and self.heap_list[largest]<self.heap_list[right]:
            largest=right

        if largest!=index:
            self.__swap(index,largest)
            self.__bubbledown(largest)

    def size(self):
        return len(self.heap_list)-1


# In[25]:


#heap Sort
input_list=list(map(int,input().rstrip().split()))
heap_obj=MaxHeap(input_list)
solution=[]
for i in range(heap_obj.size()):
    solution.append(heap_obj.pop())
print(solution[:])

