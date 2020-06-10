class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dict1={}
        
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
                
        for k,v in dict1.items():
            if v==1:
                return k