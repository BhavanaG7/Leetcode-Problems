#https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False

        i=1
        #check if strictly increasing
        while i<len(A) and A[i]>A[i-1]:
            i+=1

        #constant rate neither increasing nor decreasing
        if i==1 or i==len(A):
            return False

        #check if strictly decreasing
        while i<len(A) and A[i]<A[i-1]:
            i+=1
        
        #check and return value based on whether it has reached last value
        return i==len(A)