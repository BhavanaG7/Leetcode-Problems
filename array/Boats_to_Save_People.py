#https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left=0
        right=len(people)-1
        count=0

        while left<right:
            if left==right:
                count+=1

            if people[left]+people[right]<=limit:
                left+=1
            count+=1
            right-=1
        return count
