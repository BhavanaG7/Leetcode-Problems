#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def find_left_position(self,nums,target):
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]==target:
                if mid-1>=0 and nums[mid-1]!=target or mid==0:
                    return mid
                right=mid-1
                
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
                    
        return -1
    
    
    def find_right_position(self,nums,target):
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            
            if nums[mid]==target:
                if mid+1<len(nums) and nums[mid+1]!=target or mid==len(nums)-1:
                    return mid
                left=mid+1
                
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.find_left_position(nums,target)
        right=self.find_right_position(nums,target)
        return [left,right]